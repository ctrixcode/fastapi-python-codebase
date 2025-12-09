class ResponseErrorMessages:
    RESOURCE_NOT_FOUND = "The requested resource was not found."
    REQUEST_IS_INVALID = "The request is invalid."
    UNAUTHORIZED_ACCESS = (
        "Authentication is required and has failed or has not yet been provided."
    )
    INTERNAL_SERVER_ERROR = "An unexpected error occurred."


class ResponseMessages:
    API_IS_RUNNING = "API is running."
