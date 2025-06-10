from AgentFactory import AgentFactory
from utils import RateLimiter
from langgraph.constants import Send
from langgraph.graph import END
from GraphState.deep_research_state import SectionState, ReportState, ReportStateOutput
from GraphState.main_state import MainGraphState
from GraphState.strategist_state import StrategistState
from Agents import generate_queries, write_section, write_final_sections, generate_report_plan, compile_final_report
from Agents.search_agent import search_web
from Agents.format_section_agent import format_completed_sections
from Agents.write_section_agent import parallelize_section_writing, parallelize_final_section_writing
from Agents.rewrite_query_forStrategist_agent import RewriteQueryForStrategist
from RAG import Data as RAG_data
from Agents.strategist_retriever_agent import Retrieve_docs_for_strategist

# 將底層Agent 實例化為一個node
def transform_to_report_state(state: MainGraphState):
    """Transform MainGraphState to ReportState"""
    return {
        "topic": state.llm_transcript,
    }

def transform_to_strategist_state(state: MainGraphState):
    """Transform MainGraphState to StrategistState"""
    return {
        "user_query": state.user_query,
        "response": "",  # Initialize with empty string
        "documents": "",  # Initialize with empty list
        "rewritten_query": "",  # Initialize with empty string
        "can_doc_answer_question": True  # Initialize with True
    }

class Nodes():
    def __init__(self, llm):
        self.agent = AgentFactory(llm)     
        self.llm = llm
        self.rate_limiter = RateLimiter()

    def determine_userQuery(self, state: MainGraphState):
        user_query = state.user_query
        # Append returns None, so we need to copy the list first
        updated_query_history = state.user_query_history.copy()
        updated_query_history.append(user_query)
        result = self.agent.query_analyzer.chain.invoke(
            {"user_query": user_query})

        return {
            "user_query_history": updated_query_history,
            "user_query": result.user_query,
            "response": result.response,
            "llm_transcript": result.llm_transcript,
            "adapter_route": result.adapter_route
        }

    def retrieve_doc_for_strategist(self, state: StrategistState):
        result = Retrieve_docs_for_strategist(self.llm, RAG_data.db_collection_name_premier_league, state)

        return {
            "user_query": result["user_query"],
            "documents": result["documents"],
            "rewritten_query": result["rewritten_query"],
            "can_doc_answer_question": result["can_doc_answer_question"]
        }
    
    def rewrite_query_for_strategist(self, state: StrategistState):
        result = RewriteQueryForStrategist(self.llm, state)

        return {
            "rewritten_query": result["rewritten_query"]
        }
    
    def route_to_strategist(self, state: StrategistState):
        if state.can_doc_answer_question:
            return "Generate Analysis Report"
        else:
            return "Rewrite Query for Strategist"

    def strategist(self, state: StrategistState):
        result = self.agent.strategist.chain.invoke({
            "teams_data": state.documents,
            "user_query": state.user_query
        })
        return {
            "response": result
        }

    def route_based_to_strategist(self, state: MainGraphState):
        """
        Understand if the user query needs a strategist
        """
        if state.adapter_route == "Strategist node needed":
            return Send("Strategist", transform_to_strategist_state(state))
        elif state.adapter_route == "Deep Research node needed":
            return Send("Deep Research", transform_to_report_state(state))
        else:
            return "Answer directly"

    def update_PremierLeague_data(self, state):
        """
        Update the Premier League data.
        """
        pass

    # ================================
    # Deep Research 
    # ================================
    def generate_queries(self, state: SectionState):
        self.rate_limiter.wait_if_needed("generate_queries")
        return generate_queries(self.llm, state)

    async def search_web(self, state: SectionState):
        return await search_web(state)

    def write_section(self, state: SectionState):
        self.rate_limiter.wait_if_needed("write_section")
        return write_section(self.llm, state)

    def write_final_sections(self, state: SectionState):
        self.rate_limiter.wait_if_needed("write_final_sections")
        return write_final_sections(self.llm, state) 

    async def generate_report_plan(self, state: ReportState):
        self.rate_limiter.wait_if_needed("generate_report_plan")
        return await generate_report_plan(self.llm, state)

    def compile_final_report(self, state: ReportState):
        return compile_final_report(state)

    def format_completed_sections(self, state: ReportState):
        return format_completed_sections(state)
    
    def parallelize_section_writing(self, state: ReportState):
        return parallelize_section_writing(state)

    def parallelize_final_section_writing(self, state: ReportState):
        return parallelize_final_section_writing(state)
    
    # ================================
    # End of Deep Research
    # ================================

