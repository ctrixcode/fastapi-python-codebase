from pydantic import BaseModel, Field


class HealthCheck(BaseModel):
    status: str = Field(default="success", description="Status of the health check")
    message: str = Field(
        default="API is running", description="Message indicating the API status"
    )
