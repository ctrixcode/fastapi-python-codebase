# src/api/v1/api.py
from fastapi import APIRouter

from src.features.examples.router import router as example_router

api_router = APIRouter()
api_router.include_router(example_router, prefix="/examples", tags=["examples"])
