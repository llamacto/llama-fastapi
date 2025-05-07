from fastapi import APIRouter

# Create web router
web_router = APIRouter()

@web_router.get("/")
async def home():
    return {
        "message": "Welcome to Llama FastAPI",
        "docs": "/docs",
        "health": "/health"
    }
