from AgentFactory import AgentFactory
from Agents.prompts import list_of_teams, format_df_as_str_dict, create_team_data_report
from Scrapper.PrimerLeague import PremierLeagueCrawler
# 將底層Agent 實例化為一個node

class Nodes():
    def __init__(self, llm):
        self.agent = AgentFactory(llm)
        self.teams_data = {}

        for teamName in list_of_teams:
            team_data = PremierLeagueCrawler.loadTeamsInfo(f"Teams/{teamName}_stats.xlsx")
            self.teams_data[teamName] = team_data

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
        user_query = state.user_query
        list_of_teams = state.list_of_teams

        tmp_team_data_str = []
        team_data_to_LLM = ""
        for teamName in list_of_teams:
            for worksheetName, df in self.teams_data[teamName].items():
                tmp_team_data_str.append(format_df_as_str_dict(worksheetName, df))
            team_data_to_LLM += create_team_data_report(teamName, tmp_team_data_str)

        print(estimate_tokens(team_data_to_LLM))
        #result = ""
        result = self.agent.strategist.chain.invoke({"user_query": user_query, "all_teams_data": team_data_to_LLM})
        return {
            "response": result
        }

def estimate_tokens(text, chars_per_token=6):
    """
    根据输入文本估算令牌数。
    
    :param text: 输入文本
    :param chars_per_token: 每个令牌对应的字符数，默认为6
    :return: 估算的令牌数
    """
    return len(text) // chars_per_token