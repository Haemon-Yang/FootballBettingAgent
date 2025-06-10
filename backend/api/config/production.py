from .settings import BaseConfig

class ProductionConfig(BaseConfig):
    # Environment
    ENV: str = "production"
    
    # Frontend URL (to be set in environment variables)
    FRONTEND_URL: str = "https://your-domain.com"
    
    # API Settings
    DEBUG: bool = False
    
    # Database (if needed)
    DATABASE_URL: str = "postgresql://user:password@localhost/dbname"
    
    # AI Model Settings
    AI_MODEL: str = "gpt-4o-mini"
    AI_TEMPERATURE: float = 0.0
