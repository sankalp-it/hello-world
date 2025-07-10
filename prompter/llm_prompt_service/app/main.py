from fastapi import FastAPI
from app.routes import prompt_router

app = FastAPI(title="LLM Prompt Store")

app.include_router(prompt_router.router)
