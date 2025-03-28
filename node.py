from AgentFactory import AgentFactory
from Agents.prompts import list_of_teams
# 將底層Agent 實例化為一個node

class Nodes():
    def __init__(self, llm):
        self.agent = AgentFactory(llm)     

    def determine_userQuery(self, state):
        user_query = state.user_query
        # Append returns None, so we need to copy the list first
        updated_query_history = state.user_query_history.copy()
        updated_query_history.append(user_query)
        result = self.agent.query_analyzer.chain.invoke(
            {"user_query": user_query, "list_of_teams": list_of_teams})

        return {
            "user_query_history": updated_query_history,
            "user_query": result.user_query,
            "list_of_teams": result.list_of_teams,
            "response": result.response
        }

    def strategist(self, state):
        llm_transcript_response = state.response

        result = self.agent.strategist.chain.invoke(llm_transcript_response)
        return {
            "response": result
        }

    def update_PremierLeague_data(self, state):
        """
        Update the Premier League data.
        """
        pass