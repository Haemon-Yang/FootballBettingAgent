from Agents.query_analyzer import QueryAnalyzer
from Agents.strategist import Strategist
from Agents.generate_queries_agent import generate_queries
from Agents.write_section_agent import write_section
from Agents.report_agent import generate_report_plan
from Agents.write_section_agent import write_final_sections
from RAG import Data as RAG_data

# Factory Agent
class AgentFactory():
    def __init__(self, llm):
        self.llm = llm
        self.query_analyzer = QueryAnalyzer(llm)
        self.strategist = Strategist(llm, RAG_data.db_collection_name_premier_league)
