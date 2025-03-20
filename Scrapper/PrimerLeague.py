from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
import requests
import time
#from .scrapperData import Data
from scrapperData import Data
import csv
import os
from io import StringIO

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
            1: "StandardStats",
            2: "ShootingStats",
            3: "PassingStats", 
            4: "PassTypes",
            5: "GoalShotCreation",
            6: "DefensiveActions",
            7: "Possession",
            8: "PlayingTime",
            9: "MiscStats"
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

   def loadTeamsInfo(self, filePath: str) -> dict:
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
      
   # ToDo: 1. async scrapping 2. store into database (local & cloud) 3. Load Data
   # Additional: 1. logging monitoring
