from .messages import ResponseErrorMessages


class APIException(Exception):
    """Base class for all API exceptions."""

    def __init__(
        self,
        status_code: int,
        message: str,
        code: str,
    ):
        self.status_code = status_code
        self.message = message
        self.code = code


class NotFoundException(APIException):
    """To be raised when a resource is not found."""

    def __init__(self, message: str = ResponseErrorMessages.RESOURCE_NOT_FOUND):
        super().__init__(status_code=404, message=message, code="NOT_FOUND")


class BadRequestException(APIException):
    """To be raised for client-side errors (e.g., invalid input)."""

    def __init__(self, message: str = ResponseErrorMessages.REQUEST_IS_INVALID):
        super().__init__(status_code=400, message=message, code="BAD_REQUEST")


class UnauthorizedException(APIException):
    """To be raised for authentication errors."""

    def __init__(self, message: str = ResponseErrorMessages.UNAUTHORIZED_ACCESS):
        super().__init__(status_code=401, message=message, code="UNAUTHORIZED")
