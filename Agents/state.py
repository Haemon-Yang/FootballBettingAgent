from pydantic import BaseModel
import pandas as pd
from typing import List, Dict

# Define the state of the graph
class GraphState(BaseModel):
    user_query: str
    user_query_history: List[str]
    llm_transcribe_user_query: str
    teams_data: Dict[str, pd.DataFrame]
    response: str

