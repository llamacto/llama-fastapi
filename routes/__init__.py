from fastapi import APIRouter
from .api import api_router
from .web import web_router

# Create main router
router = APIRouter()

# Include all routers
router.include_router(web_router)
router.include_router(api_router, prefix="/api")
