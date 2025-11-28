from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .api.v1.api import api_router
from .core.database import init_db
from .core.exceptions import APIException
from .core.logger import log
from .core.messages import ResponseMessages
from .schemas.health import HealthCheck
from .schemas.response import ErrorResponse, SuccessResponse
from .core.settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan manager for the FastAPI application."""
    # Sever started
    log.info("Initializing database...")
    await init_db()
    log.info("Database initialization complete.")
    yield
    # Server stopped


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api/v1")


@app.exception_handler(APIException)
async def api_exception_handler(request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(err_code=exc.code, message=exc.message),
    )


# ==============================================================================
# ARCHITECTURAL DECISION: RATE LIMITING STRATEGY
# ==============================================================================
# Choose the implementation that fits the current infrastructure availability.
#
# OPTION A: High Performance & Distributed (RECOMMENDED for Production)
# Library: `fastapi-limiter`
# - Best for: High-load async applications running on Kubernetes/Docker Swarm.
# - Requirement: Redis (uses Lua scripts for atomic, race-condition-free counting).
# - Pros: Fully async, lowest latency overhead.
#
# OPTION B: Simplicity & Flexibility (Best for Dev/MVP)
# Library: `slowapi`
# - Best for: Single-instance apps, testing, or if Redis is not yet available.
# - Requirement: None (defaults to in-memory), but supports Redis/Memcached later.
# - Pros: No infrastructure dependencies to start, easy decorator syntax.
# ==============================================================================


@app.get(
    "/",
    tags="/",
    name="root_endpoint",
    summary="Root Endpoint",
    description="Check if the FastAPI application is running.",
    response_model=SuccessResponse[HealthCheck],
    responses={200: {"description": "Successful Response"}},
    status_code=200,
)
def root_endpoint():
    log.info("Root endpoint / reached")
    return SuccessResponse(
        data=HealthCheck(status="success", message=ResponseMessages.API_IS_RUNNING)
    )
