from fastapi import FastAPI
from typing import Dict
from .schemas.health import HealthCheck
from starlette.middleware.cors import CORSMiddleware
from .core.logger import log

app = FastAPI(title="FastAPI Python Codebase", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
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
    responses={200: {"description": "Successful Response"}},
    status_code=200,
    response_model=HealthCheck,
)
def root_endpoint():
    log.info("Root endpoint / reached")
    return HealthCheck(status="success", message="API is running")
