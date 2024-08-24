from fastapi import FastAPI
from pydantic import BaseModel

from .routers.v1 import router as api_router_v1

app = FastAPI()

app.include_router(api_router_v1)

@app.get("/")
async def root():
    return {"message": "Hello World"}
