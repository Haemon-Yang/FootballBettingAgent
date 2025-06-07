from Agents.query_analyzer import QueryAnalyzer
from Agents.strategist import Strategist

# Factory Agent
class AgentFactory():
    def __init__(self, llm):
        self.llm = llm
        self.query_analyzer = QueryAnalyzer(llm)
        self.strategist = Strategist(llm)