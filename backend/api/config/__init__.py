import os
from .development import DevelopmentConfig
from .production import ProductionConfig

def get_settings():
    env = os.getenv("ENV", "development")
    if env == "production":
        return ProductionConfig()
    return DevelopmentConfig()

settings = get_settings()
