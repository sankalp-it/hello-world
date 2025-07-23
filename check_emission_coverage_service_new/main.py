from fastapi import FastAPI
from api.router import router

app = FastAPI(title="Check Emission Coverage Service")

app.include_router(router, prefix="/check-emission", tags=["Emission Coverage"])
