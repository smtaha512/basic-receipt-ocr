from typing import Any

from fastapi import HTTPException


class BaseHttpException(HTTPException):
    def __init__(self, status_code: int, code: str, message: Any, **kwargs: Any):
        super().__init__(
            status_code=status_code,
            detail={
                "status_code": status_code,
                "code": code,
                "message": message,
                "args": kwargs,
            },
        )
