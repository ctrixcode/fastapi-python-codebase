from fastapi import FastAPI
from typing import Dict
from .schemas.health import HealthCheck
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI Python Codebase", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)


@app.get(
    "/",
    tags="/",
    name="root_endpoint",
    summary="Root Endpoint",
    description="Check if the FastAPI application is running.",
    responses={200: {"description": "Successful Response"}},
    status_code=200,
    response_model=HealthCheck,
)
def root_endpoint():
    return health_check("success", "API is running")
