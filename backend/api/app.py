from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from .router import agent_router, deep_research_router
from .config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "welcome_message": "Welcome to Your Smart Betting Assistant",
        "description": "Get real-time insights, analysis, and predictions to make informed betting decisions. \n\n Our AI-powered assistant is here to help you navigate the world of sports betting."
    }

# Include routers
app.include_router(agent_router, prefix="/api")
app.include_router(deep_research_router, prefix="/api")
