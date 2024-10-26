from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.post("/upload")
def upload_receipt() -> Any:
    return {}
