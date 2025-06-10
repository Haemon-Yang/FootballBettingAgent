from pydantic import BaseModel
from ..base import BaseResponse
from typing import Optional

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseResponse):
    response: str

class DeepResearchRequest(BaseModel):
    query: str
    context: Optional[dict] = None

class DeepResearchResponse(BaseResponse):
    response: str
    error: Optional[str] = None