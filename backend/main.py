"""FastAPI application entry point for CodeMemory."""

import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import chat, health, memory, repository

load_dotenv()

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

app = FastAPI(
    title="CodeMemory API",
    description="API for repository-aware chat, GitHub integration, and persistent developer memory.",
    version="1.0.0",
)

allowed_origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(health.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(repository.router, prefix="/api")
app.include_router(memory.router, prefix="/api")


@app.get("/", tags=["Health"])
async def root():
    return {"message": "Welcome to CodeMemory API", "docs": "/docs", "health": "/api/health"}
