from typing import Any

from fastapi import APIRouter, UploadFile
from google.cloud import vision

from .exceptions.invalid_file_type_exception import InvalidFileTypeException
from .parsers import receipt_parser

router = APIRouter()


@router.post("/upload")
async def upload_receipt(file: UploadFile) -> Any:
    if not file.content_type.startswith("image/"):
        raise InvalidFileTypeException("image", file.content_type)

    content = await file.read()

    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    return {
        "file": file.filename,
        "type": file.content_type,
        "text": receipt_parser.parse_receipt(texts),
    }
