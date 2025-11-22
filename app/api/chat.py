from app.services.llm.model_service import ModelService
from app.services.llm.prompt_service import PromptService
from app.services.llm.retrieval_service import RetrieverService
from app.services.llm.response_service import ResponseService
from app.domain.query_request import QueryRequest
from app.config.settings import Settings
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, HTTPException, Request

router = APIRouter()
settings = Settings()

modelService = ModelService(settings)
retrieverService = RetrieverService(settings)
responseService = ResponseService(settings)
promptService = PromptService()

@router.post("/chat/stream")
async def chat_stream(request: QueryRequest):
    try:
        #step 1 first retrieve the context using the retriever
        context = retrieverService.invoke(request.query)
        if not context or not str(context).strip():
            return HTMLResponse('<html>I don\'t know</html>', status_code=200) 
        
        prompt_str = promptService.invoke(request.query, context)
        model = modelService.invoke()

        responseService = ResponseService(model)
        return responseService.invoke(
            prompt_str=prompt_str
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
