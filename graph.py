from langgraph.graph import StateGraph, START, END
from GraphState.main_state import MainGraphState
from node import Nodes
from GraphState.deep_research_state import ReportState, ReportStateInput, ReportStateOutput
from GraphState.deep_research_state import SectionState, SectionOutputState
from langchain_openai import ChatOpenAI
import os
# Agent 中的最上層 用來連接所有Node

class Workflow():
    def __init__(self, llm):
        # Deep Research Workflow
        nodes = Nodes(llm)

        section_builder = StateGraph(SectionState, output=SectionOutputState)
        section_builder.add_node("generate_queries", nodes.generate_queries)
        section_builder.add_node("search_web", nodes.search_web)
        section_builder.add_node("write_section", nodes.write_section)
        section_builder.add_edge(START, "generate_queries")
        section_builder.add_edge("generate_queries", "search_web")
        section_builder.add_edge("search_web", "write_section")
        section_builder.add_edge("write_section", END)
        section_builder_subagent = section_builder.compile()

        # Add nodes and edges
        deep_research_workflow = StateGraph(ReportState, input= ReportStateInput, output=ReportStateOutput)
        
        deep_research_workflow.add_node("generate_report_plan", nodes.generate_report_plan)
        deep_research_workflow.add_node("section_builder_with_web_search", section_builder_subagent)
        deep_research_workflow.add_node("format_completed_sections", nodes.format_completed_sections)
        deep_research_workflow.add_node("write_final_sections", nodes.write_final_sections)
        deep_research_workflow.add_node("compile_final_report", nodes.compile_final_report)

        deep_research_workflow.add_edge(START, "generate_report_plan")
        deep_research_workflow.add_conditional_edges("generate_report_plan",
                                    nodes.parallelize_section_writing,
                                    ["section_builder_with_web_search"])
        deep_research_workflow.add_edge("section_builder_with_web_search", "format_completed_sections")
        deep_research_workflow.add_conditional_edges("format_completed_sections",
                                    nodes.parallelize_final_section_writing,
                                    ["write_final_sections"])
        deep_research_workflow.add_edge("write_final_sections", "compile_final_report")
        deep_research_workflow.add_edge("compile_final_report", END)
        
        deep_research_agent = deep_research_workflow.compile()

        #==========================

        # Main Workflow
        workflow = StateGraph(MainGraphState)
        workflow.add_node("Understand User Query", nodes.determine_userQuery)
        workflow.add_node("Strategist", nodes.strategist)
        workflow.add_node("Deep Research", deep_research_agent)

        workflow.add_edge(START, "Understand User Query")
        
        # Future: Add conditional edge (if query do not need strategist, then answer it directly)
        workflow.add_conditional_edges(
            "Understand User Query",
            nodes.route_based_to_strategist,
            {
                "Strategist node needed": "Strategist",
                "Deep Research node needed": "Deep Research", 
                "Answer directly": END
            }
        )
        
        workflow.add_edge("Strategist", END)      
        workflow.add_edge("Deep Research", END)

        self.app = workflow.compile()

    @staticmethod
    # Function to fetch response from workflow
    async def fetch_response(workflow, initial_state, result_container):
        # Execute the workflow and get the response
        result = await workflow.app.ainvoke(initial_state)
        result_container["response"] = result["response"]
        result_container["done"] = True

def visualize_workflow():
    # Initialize workflow with SurveyNode directly
    llm = ChatOpenAI(model="gpt-4o-mini")
    workflow = Workflow(llm)
    
    # Get the graph before compilation
    graph = workflow.app
    
    graph_image = graph.get_graph().draw_mermaid_png()
    # Save the image
    output_dir = "Doc/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(os.path.join(output_dir, "workflow_graph.png"), "wb") as f:
        f.write(graph_image)
    
    print("Graph has been saved as 'Docs/workflow_graph.png'")

if __name__ == "__main__":
    visualize_workflow()