from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from config.config import settings
from config.security import create_access_token, verify_password
from database.session import get_db
from app.user import services as user_services
from app.user.schemas import UserCreate
from . import schemas
import logging
from app.common.schemas.base_response import BaseResponse

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/register", response_model=BaseResponse)
async def register(
    request: schemas.RegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    """用户注册"""
    try:
        # 验证密码
        if request.password != request.confirm_password:
            return BaseResponse(code=400, msg="Passwords do not match")
        
        # 检查邮箱是否已注册
        db_user = await user_services.get_user_by_email(db, email=request.email)
        if db_user:
            return BaseResponse(code=400, msg="Email already registered")
        
        # 创建用户
        user = await user_services.create_user(
            db=db,
            user=UserCreate(
                email=request.email,
                password=request.password
            )
        )
        
        # 生成访问令牌
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=access_token_expires
        )
        return BaseResponse(data={
            "access_token": access_token,
            "token_type": "bearer"
        })
    except Exception as e:
        logger.error(f"注册失败: {str(e)}", exc_info=True)
        return BaseResponse(code=500, msg="Internal Server Error", data=str(e))


@router.post("/login", response_model=BaseResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """用户登录"""
    try:
        user = await user_services.authenticate_user(
            db=db,
            email=form_data.username,
            password=form_data.password
        )
        if not user:
            return BaseResponse(code=401, msg="Incorrect email or password")
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=access_token_expires
        )
        return BaseResponse(data={
            "access_token": access_token,
            "token_type": "bearer"
        })
    except Exception as e:
        logger.error(f"登录失败: {str(e)}", exc_info=True)
        return BaseResponse(code=500, msg="Internal Server Error", data=str(e)) 