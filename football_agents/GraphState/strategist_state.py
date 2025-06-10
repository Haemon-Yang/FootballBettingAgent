from pydantic import BaseModel
import pandas as pd
from typing import List, Dict
from langchain_core.documents import Document

# Define the state of the graph
class StrategistState(BaseModel):
    user_query: str
    response: str
    documents: str
    rewritten_query: str

    can_doc_answer_question: bool
