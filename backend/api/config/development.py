from .settings import BaseConfig

class DevelopmentConfig(BaseConfig):
    # Environment
    ENV: str = "development"
    
    # Frontend URL
    FRONTEND_URL: str = "http://localhost:5173"
    
    # API Settings
    DEBUG: bool = True
    
    # Database (if needed)
    #DATABASE_URL: str = "sqlite:///./dev.db"
    
    # AI Model Settings
    AI_MODEL: str = "gpt-4o-mini"
    AI_TEMPERATURE: float = 0.0
