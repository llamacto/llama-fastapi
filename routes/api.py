from fastapi import APIRouter
from app.auth.api import router as auth_router
from app.user.api import router as user_router
from app.article.api import router as article_router

# Create API router
api_router = APIRouter()

# Register all API routes
api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(user_router, prefix="/users", tags=["Users"])
api_router.include_router(article_router, prefix="/articles", tags=["Articles"])

# Health check route
@api_router.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}
