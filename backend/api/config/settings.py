from pydantic_settings import BaseSettings
from typing import Optional
import os

class BaseConfig(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Football Betting AI"
    DEBUG: bool = False
    FRONTEND_URL: str = "http://localhost:8501"
    
    # Security
    SECRET_KEY: Optional[str] = None
    
    # API Keys
    OPENAI_API_KEY: str
    LANGCHAIN_API_KEY: str
    TAVILY_API_KEY: str
    HUGGINGFACE_API_KEY: str
    
    # LangSmith Settings
    LANGSMITH_PROJECT: str
    LANGSMITH_API_KEY: str
    LANGSMITH_TRACING: str = "true"
    
    class Config:
        # Look for .env file in the root directory (two levels up from this file)
        env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), ".env")
        case_sensitive = True

settings = BaseConfig()
