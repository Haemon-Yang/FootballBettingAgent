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
            {"user_query": user_query})

        return {
            "user_query_history": updated_query_history,
            "user_query": result.user_query,
            "response": result.response,
            "is_strategist_needed": result.is_strategist_needed
        }

    def strategist(self, state):
        llm_transcript_response = state.response

        result = self.agent.strategist.chain.invoke(llm_transcript_response)
        return {
            "response": result
        }

    def route_based_to_strategist(self, state):
        """
        Understand if the user query needs a strategist
        """
        if state.is_strategist_needed == True:
            return "YES"
        else:
            return "NO"

    def update_PremierLeague_data(self, state):
        """
        Update the Premier League data.
        """
        pass