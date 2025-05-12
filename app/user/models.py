from sqlalchemy import Boolean, Column, Integer, String
from database.base import Base


class User(Base):
    """User model"""
    __tablename__ = "users"
    # 添加 extend_existing=True 解决表重复定义问题
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False) 