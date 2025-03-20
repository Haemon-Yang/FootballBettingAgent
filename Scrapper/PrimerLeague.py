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
         standardStats = pd.read_html(StringIO(dataText.text), match="Standard Stats")
         playerShootingStats = pd.read_html(StringIO(dataText.text), match="Shooting")
         playerPassingStats = pd.read_html(StringIO(dataText.text), match="Passing")
         playerPassTypes = pd.read_html(StringIO(dataText.text), match="Pass Types")
         playerGoalandShotCreaterion = pd.read_html(StringIO(dataText.text), match="Goal and Shot Creation")
         playerDefensiveActions = pd.read_html(StringIO(dataText.text), match="Defensive Actions")
         playerPossession = pd.read_html(StringIO(dataText.text), match="Possession")
         playerPlayingTime = pd.read_html(StringIO(dataText.text), match="Playing Time")
         playerMisc = pd.read_html(StringIO(dataText.text), match="Miscellaneous Stats")
         return [matches, standardStats, 
                 playerShootingStats, playerPassingStats, playerPassTypes, playerGoalandShotCreaterion, 
                 playerDefensiveActions, playerPossession, playerPlayingTime, playerMisc]

      except Exception as e:
         print(f"Error in scrap: {e}")
   
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

   def uploadTeamsStatsToDatabase(self, teamsStats: list[pd.DataFrame]):
      pass 

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

if __name__ == "__main__":
   crawler = PremierLeagueCrawler()
   crawler.getTeamsUrl()
   crawler.scrap()
   print(crawler.teamsName[0])