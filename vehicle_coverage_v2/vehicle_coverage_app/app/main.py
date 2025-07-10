from fastapi import FastAPI
from app.api.coverage_controller import router as coverage_router

app = FastAPI(title="Vehicle Coverage API")
app.include_router(coverage_router, prefix="/api")
