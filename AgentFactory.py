from Agents.query_analyzer import QueryAnalyzer
from Agents.strategist import Strategist
from RAG import Data as RAG_data

# Factory Agent
class AgentFactory():
    def __init__(self, llm):
        self.llm = llm
        self.query_analyzer = QueryAnalyzer(llm)
        self.strategist = Strategist(llm, RAG_data.db_collection_name_premier_league)
