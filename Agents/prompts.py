import pandas as pd
from typing import List, Dict

DetermineUserQuery_template = [
    ("system", """You are a expert at analyzing user queries to clearly identify their underlying requirements, intentions, and constraints. Carefully read the user's message below, and then:

     You are also an expert at football betting game.
    
1. Extract and list the user's main requirements or goals.
2. Identify any constraints, conditions, or specifications mentioned explicitly or implicitly by the user.
3. Summarize the user's overall intent clearly and concisely.
4. Suggest clarifying questions if any ambiguity or uncertainty remains.
5. Ensure the query can retrieves accurate and complete information from the RAG system. Some content may be split across chunks, so try to reconstruct or retrieve the full context where possible.
6. Make sure if the user query requires a strategist node or not.       
7. If the user's query is unrelated to the expected domain or task, still respond appropriately in the "response" field. 
You may provide helpful, general-purpose information or gently redirect the user back on topic.
Do not reject the question outright unless it violates safety policies.
      
Note: 
     - strategist node is only needed if the user query requires a detailed analysis.
     - Respond to the user's query in the "response" field.
     - Output your understanding of the user's query in the "llm_transcript" field.

     {format_instructions}
     """),
    ("user", "Analyze the following user query: {user_query}")
]

strategist_template = [
    ("system", """
    You're a professional football betting agent with enhanced analytical autonomy.

    Guidelines: 
    0. Use the retrieved statistics to support your analysis
    1. Provide detailed analyses and insightful predictions for upcoming matches.
    2. Clearly state your reasoning for each recommendation, and suggest optimal betting strategies to maximize returns.
    3. In addition to your existing expertise, you now possess the ability to autonomously analyze raw data by deriving quantifiable indicators. 
        - Use these indicators - derived directly from the raw data I provided - to support your analyses and scientific reasoning. 
        - If further indicators can be deduced by combining initial indicators with other data points, that is allowed; however, generate only as many indicators as needed to quantify the data and substantiate your recommendations based on the depth of the inquiry.
    4. If the retrieved information is insufficient, acknowledge the limitations.
     """),
    ("user", """
     User query: {user_query}
     
     Data: {teams_data}
     """)
]

list_of_teams = [
    "Southampton",
    "Leicester City",
    "Ipswich Town",
    "Wolves",
    "West Ham",
    "Everton",
    "Tottenham",
    "Manchester Utd",
    "Crystal Palace",
    "Brentford",
    "Bournemouth",
    "Aston Villa",
    "Fulham",
    "Brighton",
    "Newcastle Utd",
    "Manchester City",
    "Chelsea",
    "Nott'ham Forest",
    "Arsenal",
    "Liverpool"
]

def format_df_as_str_dict(worksheetName:str, df: pd.DataFrame) -> Dict[str, str]:
    """
    Transform a pandas DataFrame into a string representation.

    Returns:
    dict: {worksheetName, dataframeInStr}

    Note: works only for single team data.
    """
    return {worksheetName: df.to_string()}

def create_team_data_report(teamName: str, teamData: List[dict]) -> str:
    """
    Combine multiple dataframe string representations into a complete string format of team data.

    Args:
        teamName (str): The name of the team.
        teamData (List[dict]): List of dictionaries containing dataframe string representations.
            Each dictionary should contain dataframe information converted to string format.
    
    Returns:
        str: A complete string representation of all team data combined into a single formatted string.
            This string contains all the teams information aggregated from multiple dataframes.
    """
    teamDataStr = f"Team: {teamName}\n\n"

    for team in teamData:
        for worksheetName, dataframeInStr in team.items():
            teamDataStr += f"Data - {worksheetName}:\n\n {dataframeInStr}\n\n"
            teamDataStr += "-----------------------------------\n\n"
    #teamDataStr += f"{teamName} Data End\n"
    teamDataStr += "===================================\n\n"
    
    return teamDataStr