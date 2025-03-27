from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
import requests
import time
from .scrapperData import Data
import os
from io import StringIO
from langchain_openai import ChatOpenAI
from typing import List, Dict
from Agents.prompts import format_df_as_str_dict, create_team_data_report_md

class PremierLeagueCrawler:
   data = requests.get(Data.ScrappedUrl, headers = Data.get_headers())
   soup = BeautifulSoup(data.text, 'html.parser')
   teamsInfo = {} # store Teams Name & url

   def __init__(self):
      pass

   # Update all teams
   def scrap(self, url: str) -> list[pd.DataFrame]:
      try:
         delay = np.random.uniform(2, 5)
         time.sleep(delay)
         dataText = requests.get(url, headers=Data.get_headers())
         matches = pd.read_html(StringIO(dataText.text), match="Scores & Fixtures")
         playerstandardStats = pd.read_html(StringIO(dataText.text), match="Standard Stats")
         playerShootingStats = pd.read_html(StringIO(dataText.text), match="Shooting")
         playerPassingStats = pd.read_html(StringIO(dataText.text), match="Passing")
         playerPassTypes = pd.read_html(StringIO(dataText.text), match="Pass Types")
         playerGoalandShotCreaterion = pd.read_html(StringIO(dataText.text), match="Goal and Shot Creation")
         playerDefensiveActions = pd.read_html(StringIO(dataText.text), match="Defensive Actions")
         playerPossession = pd.read_html(StringIO(dataText.text), match="Possession")
         playerPlayingTime = pd.read_html(StringIO(dataText.text), match="Playing Time")
         playerMisc = pd.read_html(StringIO(dataText.text), match="Miscellaneous Stats")
         return [matches, playerstandardStats, 
                 playerShootingStats, playerPassingStats, playerPassTypes, playerGoalandShotCreaterion, 
                 playerDefensiveActions, playerPossession, playerPlayingTime, playerMisc]

      except Exception as e:
         print(f"Error in scrap: {e}")

   def preprocess_data(self, data_list: list[pd.DataFrame]) -> list[pd.DataFrame]:
      cleaned_data_list = []
      for df in data_list:
         cols_to_keep = []
         for col in df[0].columns:
            if type(col) == str:
               if col == "Notes" or col == "Match Report" or col == "Referee":
                  df[0].drop(col, axis=1, inplace=True)
            elif type(col) == tuple:
               multi_index = tuple()
               if "Matches" in col or "Nation" in col:
                  df[0].drop(col, axis=1, inplace=True)
               else:
                  for col_name in col:                    
                     # Unnamed 則替換保留
                     if "Unnamed" in col_name:
                        multi_index += ("",)
                     else:
                        multi_index += (col_name,)
                  cols_to_keep.append(multi_index)

         if cols_to_keep == []:
            cleaned_data_list.append(df[0])
         else:
            df[0].columns = pd.MultiIndex.from_tuples(new_col_name for new_col_name in cols_to_keep)
            cleaned_data_list.append(df[0])
      return cleaned_data_list
   
   def save_data(self, data_list: list[pd.DataFrame], team_name: str, output_dir: str = "data", save_as_excel: bool = True) -> None:
      """
      Save scraped data either as separate CSV files or as a single Excel file with multiple worksheets.
      
      Args:
          data_list (list[pd.DataFrame]): List of DataFrames returned by scrap()
          team_name (str): Name of the team for file naming
          output_dir (str): Directory to save the files
          save_as_excel (bool): If True, save as Excel file; otherwise save as separate CSV files
      """
      try:
         # Create directory if it doesn't exist
         os.makedirs(output_dir, exist_ok=True)
         
         # Dictionary mapping DataFrames to worksheet names
         sheet_names = {
            0: "Matches",
            1: "Standard Stats",
            2: "Shooting Stats",
            3: "Passing Stats", 
            4: "Pass Types",
            5: "Goal & Shot Creation",
            6: "Defensive Actions",
            7: "Possession",
            8: "Playing Time",
            9: "Miscellaneous Stats"
         }
         
         if save_as_excel:
            # Save as Excel file with multiple worksheets
            file_path = os.path.join(output_dir, f"{team_name}_stats.xlsx")
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
               for i, df in enumerate(data_list):
                  if not df[0].empty:
                     # Get the first DataFrame if the result is a list of DataFrames
                     sheet_df = df[0] if isinstance(df, list) else df
                     sheet_name = sheet_names.get(i, f"Sheet_{i}")
                     sheet_df.to_excel(writer, sheet_name=sheet_name, index=True)
            print(f"Data saved to Excel file: {file_path}")
         else:
            # Save as separate CSV files
            for i, df in enumerate(data_list):
               if i < len(df) and not df[0].empty:
                  sheet_df = df[0] if isinstance(df, list) else df
                  sheet_name = sheet_names.get(i, f"Sheet_{i}")
                  file_path = os.path.join(output_dir, f"{team_name}_{sheet_name}.csv")
                  sheet_df.to_csv(file_path, index=True)
            print(f"Data saved as CSV files in directory: {output_dir}")
      
      except Exception as e:
         print(f"Error saving data: {e}")

   def scrapSquadStats(self, url: str) -> list[pd.DataFrame]:
      return []
  
   # Get all Teams Name & url
   def getTeamsUrl(self):
      try:         
         # Select Table 
         premierLeague = PremierLeagueCrawler.soup.select(Data.targetTable)[0]
         # Select Link
         links = premierLeague.find_all("a")

         for link in links:
            # Get Team Name
            if '/squads/' in link.get("href"):
               teamName = link.text
            url = link.get("href")
            if '/squads/' in url:
               url = url
               PremierLeagueCrawler.teamsInfo.update({teamName: f"https://fbref.com{url}"})
      except Exception as e:
         print(f"Error in getTeamsUrl: {e}")

   @staticmethod
   def loadTeamsInfo(filePath: str) -> dict:
      """
      Loads the teams info from the file.
      
      Args:
          filePath (str): Path to the file containing the teams info
      Returns:
          dict[str, pd.DataFrame]: Dictionary where keys are sheet names and values are the 
          corresponding DataFrames
      Example:
         {
            "Matches": pd.DataFrame(...),  # DataFrame with match data
            "StandardStats": pd.DataFrame(...),  # DataFrame with standard statistics
            "ShootingStats": pd.DataFrame(...)  # DataFrame with shooting statistics
         }
      """
      if not os.path.exists(filePath):
         print(f"Error: File '{filePath}' does not exist")
         return pd.DataFrame()
      try:
         df = pd.read_excel(filePath, sheet_name=None)
         return df
      except Exception as e:
        print(f"Error loading CSV file: {e}")
        return pd.DataFrame()

   @staticmethod
   def load_md_as_str(filePath: str) -> str:
      with open(filePath, encoding="utf-8") as file:
         content = file.read()
      return content
   
   @staticmethod
   def _private_process_teamData_to_prompt(filePath: str, team_name: str) -> List[str]:
      """
      Process team data to prompt.
      For LLM to generate formatted output from table data.

      Args:
         team_data (Dict[str, pd.DataFrame]): Dictionary of DataFrames with team name as key

      Returns:
         List[str]: List of prompts
      """
      team_data = PremierLeagueCrawler.loadTeamsInfo(filePath)
      prompt = []
      
      for worksheet_name, df in team_data.items():
         tmp_str = []
         tmp_str.append(format_df_as_str_dict(worksheet_name, df))
         tmp_prompt = Data.prompt.format(table_content = create_team_data_report_md(
            team_name, tmp_str))
         prompt.append(tmp_prompt)
      return prompt

   @staticmethod
   def transform_xlsx_to_md(data_to_transform: List[str], team_name: str):
      """
      Transform team data to md.
      """
      llm = ChatOpenAI(model="gpt-4o-mini")

      content = ""
      for worksheet in data_to_transform:
         llm_output = llm.invoke(input=worksheet)
         content += llm_output.content
         content += "\n\n"
         time.sleep(5)
      
      with open(f'{team_name}_all_stats.md', 'w', encoding='utf-8') as file:
         file.write(content)

   # ToDo: 1. async scrapping 2. store into database (local & cloud) 3. Load Data
   # Additional: 1. logging monitoring
