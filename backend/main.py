from fastapi import FastAPI

from .modules import app_routes

app = FastAPI(
    title="Basic Receipt OCR",
)


app.include_router(app_routes.router)
