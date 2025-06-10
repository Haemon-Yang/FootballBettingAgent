from pydantic import BaseModel
from typing import Optional

class BaseResponse(BaseModel):
    status: str
    message: Optional[str] = None
