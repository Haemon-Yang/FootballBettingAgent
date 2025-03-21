from langgraph.graph import StateGraph, START, END
from Agents.state import GraphState
from node import Nodes

# Agent 中的最上層 用來連接所有Node

class Workflow():
    def __init__(self, llm):
        workflow = StateGraph(GraphState)
        nodes = Nodes(llm)

        workflow.add_node("Understand User Query", nodes.determine_userQuery)
        workflow.add_node("Strategist", nodes.strategist)

        workflow.add_edge(START, "Understand User Query")
        
        # Future: Add conditional edge (if query do not need strategist, then answer it directly)
        workflow.add_edge("Understand User Query", "Strategist")
        
        workflow.add_edge("Strategist", END)

        self.app = workflow.compile()

    def get_initial_state(self):
        return {
        "user_query": "",
        "user_query_history": [],
        "list_of_teams": [],
        "response": ""
    }