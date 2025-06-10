from fastapi import APIRouter, HTTPException
from ...models.schemas.agent import DeepResearchRequest, DeepResearchResponse
from football_agents.graph import Workflow
from langchain_openai import ChatOpenAI
from ...config import settings

router = APIRouter(prefix="/deep-research", tags=["deep-research"])

# Initialize workflow once
llm = ChatOpenAI(model=settings.AI_MODEL)
workflow = Workflow(llm)

@router.post("/analyze", response_model=DeepResearchResponse)
async def deep_research_analysis(request: DeepResearchRequest):
    try:
        # Create initial state with user query
        initial_state = {
            "user_query": request.query,
            "context": request.context or {}
        }
        
        # Process the query using deep research workflow
        result_container = {"response": None, "done": False}
        await Workflow.fetch_response(workflow.deep_research_app, initial_state, result_container)
        
        return DeepResearchResponse(
            response=result_container["response"],
            status="success"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error in deep research analysis: {str(e)}"
        )
