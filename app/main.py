from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import HTMLResponse
import httpx

from app.middlewares.cors_middleware import CorsMiddleware
from app.middlewares.token_middleware import TokenMiddleware
from app.api.auth import router as auth_router
from app.api.chat import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize heavy objects
    # app.state.config = Config()
    # app.state.retriever = Retriever(app.state.config)
    # app.state.prompter = Prompter()
    # app.state.model_helper = ModelHelper(app.state.config)

     # Initialize LLM once at startup
    #app.state.llm = app.state.model_helper.invoke()
    print("Startup completed")
    yield
    print("Shutdown cleanup")

app = FastAPI(title="CampusAI API", 
              description="API for question answering using retriever + CampusAI",
              version="1.0.0",
              lifespan=lifespan)

app.add_middleware(TokenMiddleware)
app.add_middleware(CorsMiddleware)

app.include_router(auth_router, prefix="/api/v1", tags=["Auth"])
app.include_router(chat_router, prefix="/api/v1", tags=["Chat"])

# HEALTH CHECK
@app.get("/health")
def root():
    return {"status": "ok", "message": "Campus API is running"}



