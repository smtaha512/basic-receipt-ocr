from typing import Any

from .base_http_exception import BaseHttpException


class BadRequestException(BaseHttpException):
    def __init__(self, code: str, message: Any, **kwargs: Any):
        super().__init__(400, code, message, **kwargs)
