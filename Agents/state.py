from pydantic import BaseModel
import pandas as pd
from typing import List, Dict

# Define the state of the graph
class GraphState(BaseModel):
    user_query: str
    user_query_history: List[str]
    list_of_teams: List[str]
    response: str