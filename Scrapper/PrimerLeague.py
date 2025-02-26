from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
import requests
import time
from .scrapperData import Data
import csv
import os
from io import StringIO

class PremierLeagueCrawler:
   data = requests.get(Data.ScrappedUrl, headers = Data.get_headers())
   soup = BeautifulSoup(data.text, 'html.parser')
   teamsUrl = []
   teamsName = []
   teamsInfo = {} # store Scores & Fixtures Dataframe

   def __init__(self):
      pass

   # Update all teams
   def scrap(self):
      try:
         idx = 0
         for url in PremierLeagueCrawler.teamsUrl:
            delay = np.random.uniform(2, 5)
            time.sleep(delay)
            dataText = requests.get(url, headers=Data.get_headers())
            matches = pd.read_html(StringIO(dataText.text), match="Scores & Fixtures")
            PremierLeagueCrawler.teamsInfo.update({PremierLeagueCrawler.teamsName[idx]: matches})
            idx += 1
            self.saveTeams()
      except Exception as e:
         print(f"Error in scrap: {e}")

   def getTeams(self):
      try:         
         # Select Table 
         premierLeague = PremierLeagueCrawler.soup.select(Data.targetTable)[0]
         # Select Link
         links = premierLeague.find_all("a")
         links = [l.get("href") for l in links]
         links = [l for l in links if '/squads/' in l]
         PremierLeagueCrawler.teamsUrl = [f"https://fbref.com{l}" for l in links]
         # Teams
         for team in premierLeague.find_all("a"):
            if '/squads/' in team.get("href"):
               PremierLeagueCrawler.teamsName.append(team.text)
      except Exception as e:
         print(f"Error in getTeamsUrl: {e}")

   def saveTeams(self):
      try:
         for team_name, team_data in self.teamsInfo.items():
            fileName = f"{team_name}.csv"
            filePath = os.path.join(Data.filePath, fileName)
            
            if isinstance(team_data[0], pd.DataFrame):
               with open(filePath, 'w', newline='', encoding='utf-8') as f:
                  team_data[0].to_csv(f, index=False)
            else:
               print(f"Warning: Data for {team_name} is not in DataFrame format")
         
      except Exception as e:
         print(f"Error saving teams data: {e}")       

   def loadTeamsInfo(self, filePath: str) -> pd.DataFrame:
      if not os.path.exists(filePath):
         print(f"Error: File '{filePath}' does not exist")
         return pd.DataFrame()
      try:
         df = pd.read_csv(filePath)
         return df
      except Exception as e:
        print(f"Error loading CSV file: {e}")
        return pd.DataFrame()
      
   # ToDo: 1. async scrapping 2. store into database (local & cloud) 3. Load Data
   # Additional: 1. logging monitoring

#if __name__ == "__main__":
#   crawler = PremierLeagueCrawler()
#   print(crawler.teamsName[0])