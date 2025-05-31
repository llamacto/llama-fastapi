from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from sqlalchemy import text
from app.common.schemas.base_response import BaseResponse

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Basic health check endpoint
    """
    return BaseResponse(data={
        "status": "healthy",
        "service": "llama-fastapi"
    })


@router.get("/health/db")
async def db_health_check(db: Session = Depends(get_db)):
    """
    Database health check endpoint
    """
    try:
        # Try to execute a simple query
        db.execute(text("SELECT 1"))
        return BaseResponse(data={
            "status": "healthy",
            "database": "connected"
        })
    except Exception as e:
        return BaseResponse(code=500, msg="Database disconnected", data=str(e)) 