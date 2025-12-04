from fastapi import APIRouter

from src.api.v1.examples import router as example_router

api_router = APIRouter()
api_router.include_router(example_router, prefix="/examples", tags=["examples"])
