from app.services.llm.model_service import ModelService
from app.services.llm.prompt_service import PromptService
from app.services.llm.retrieval_service import RetrieverService
from app.services.llm.response_service import ResponseService
from app.domain.query_request import QueryRequest
from app.config.settings import Settings

from fastapi import APIRouter, HTTPException, Request

router = APIRouter()
settings = Settings()

modelService = ModelService(settings)
retrieverService = RetrieverService(settings)
responseService = ResponseService(settings)
promptService = PromptService()

#@router.post("/chat/stream")
#async def chat_stream(request: QueryRequest):
 
