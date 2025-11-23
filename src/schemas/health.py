from pydantic import BaseModel, Field


class HealthCheck(BaseModel):
    message: str = Field(
        default="API is running", description="Message indicating the API status"
    )
