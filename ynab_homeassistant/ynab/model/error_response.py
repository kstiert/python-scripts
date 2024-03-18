class ErrorResponse:
    id: str
    name: str
    detail: str


class ErrorWrapper:
    error: ErrorResponse
