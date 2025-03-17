from AgentFactory import AgentFactory
# 將底層Agent 實例化為一個node

class Nodes():
    def __init__(self, llm):
        self.agent = AgentFactory(llm)

    def determine_userQuery(self, state):
        user_query = state.user_query
        query_history = state.append(user_query)
        result = self.agent.query_analyzer.chain.invoke({"user_query": user_query})

        return {
            **state,
            "user_query_history": query_history,
        }
