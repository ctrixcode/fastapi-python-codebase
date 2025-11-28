from pydantic import BaseModel, Field
from typing import TypeVar, Generic

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    success: bool = Field(default=True, description="Response status")
    data: T = Field(..., description="Response data")


class ErrorResponse(BaseModel):
    success: bool = Field(default=False, description="Response status")
    err_code: str = Field(..., description="Error code")
    message: str = Field(..., description="Error message")
