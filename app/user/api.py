from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from config.deps import get_current_active_user
from database.session import get_db
from . import services, schemas
from app.common.schemas.base_response import BaseResponse

router = APIRouter()


@router.post("/", response_model=BaseResponse)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await services.get_user_by_email(db, email=user.email)
    if db_user:
        return BaseResponse(code=400, msg="Email already registered")
    user_obj = await services.create_user(db=db, user=user)
    return BaseResponse(data=user_obj)


@router.get("/", response_model=BaseResponse)
async def read_users(
    skip: int = 0, 
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_active_user)
):
    """获取用户列表"""
    users = await services.get_users(db, skip=skip, limit=limit)
    return BaseResponse(data=users)


@router.get("/me", response_model=BaseResponse)
async def read_current_user(
    current_user = Depends(get_current_active_user)
):
    """获取当前登录用户信息"""
    return BaseResponse(data=current_user)


@router.get("/{user_id}", response_model=BaseResponse)
async def read_user(
    user_id: int, 
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_active_user)
):
    """获取特定用户信息"""
    user = await services.get_user(db, user_id=user_id)
    if user is None:
        return BaseResponse(code=404, msg="User not found")
    return BaseResponse(data=user)


@router.get("/{user_id}/profile", response_model=BaseResponse)
async def get_user_profile(user_id: int, db: AsyncSession = Depends(get_db)):
    """获取用户详细资料"""
    db_user = await services.get_user(db, user_id=user_id)
    if db_user is None:
        return BaseResponse(code=404, msg="User not found")
    return BaseResponse(data=db_user)


@router.put("/{user_id}/status", response_model=BaseResponse)
async def update_user_status(
    user_id: int, 
    is_active: bool, 
    db: AsyncSession = Depends(get_db)
):
    """更新用户状态"""
    db_user = await services.get_user(db, user_id=user_id)
    if db_user is None:
        return BaseResponse(code=404, msg="User not found")
    db_user.is_active = is_active
    await db.commit()
    await db.refresh(db_user)
    return BaseResponse(data=db_user) 