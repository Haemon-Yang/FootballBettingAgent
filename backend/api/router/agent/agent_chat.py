from fastapi import APIRouter, HTTPException
from ...models.schemas.agent import MessageRequest, MessageResponse
from football_agents.graph import Workflow
from langchain_openai import ChatOpenAI
from ...config import settings
import traceback

router = APIRouter(tags=["agent"])

# 初始化工作流
llm = ChatOpenAI(model=settings.AI_MODEL)
workflow = Workflow(llm)

@router.post("/agent/chat", response_model=MessageResponse)
async def send_message(request: MessageRequest):
    try:
        # 创建包含用户消息的初始状态
        initial_state = {
            "user_query": request.message,
            "user_query_history": [],
            "response": "",
            "llm_transcript": "",           
            "adapter_route": "",

        }

        # 未來還需要紀錄chat history的功能，不然每次都init，Message都沒了
        
        # 使用工作流处理消息
        result_container = {"response": None, "done": False}
        await Workflow.fetch_response(workflow.main_app, initial_state, result_container)
        
        return MessageResponse(
            response=result_container["response"],
            status="success"
        )
    except Exception as e:
        error_details = f"Error processing message: {str(e)}\nTraceback:\n{traceback.format_exc()}"
        print(error_details)  # Print to server logs
        raise HTTPException(
            status_code=500,
            detail=error_details
        )
