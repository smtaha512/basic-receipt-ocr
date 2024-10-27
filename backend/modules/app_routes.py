from fastapi import APIRouter

from .receipts import receipts_routes

router = APIRouter()

router.include_router(receipts_routes.router, prefix="/receipts", tags=["receipts"])
