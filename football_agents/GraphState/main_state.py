from pydantic import BaseModel
import pandas as pd
from typing import List, Dict

# Define the state of the graph
class MainGraphState(BaseModel):
    user_query: str
    user_query_history: List[str]
    response: str
    llm_transcript: str

    adapter_route: str # for query analyzer to determine the route of the workflow
