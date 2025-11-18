from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Python Codebase", version="1.0.0")


class health_check(BaseModel):
    status: str = Field(default="success", description="Status of the health check")
    message: str = Field(
        default="API is running", description="Message indicating the API status"
    )


@app.get(
    "/",
    tags="/",
    name="root_endpoint",
    summary="Root Endpoint",
    description="Check if the FastAPI application is running.",
    responses={200: {"description": "Successful Response"}},
    status_code=200,
    response_model=health_check,
)
def root_endpoint():
    return health_check("success", "API is running")
