from Agents.query_analyzer import QueryAnalyzer

# Factory Agent
class AgentFactory():
    def __init__(self, llm):
        self.llm = llm
        self.query_analyzer = QueryAnalyzer(llm)
