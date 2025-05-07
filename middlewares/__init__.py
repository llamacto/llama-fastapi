from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

def setup_middlewares(app: FastAPI) -> None:
    """Set up all middlewares for the application"""
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
