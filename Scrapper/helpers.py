from typing import Dict, List
import pandas as pd

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