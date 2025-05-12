from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


class ArticleBase(BaseModel):
    title: str
    content: str
    author_id: int


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


@router.post("/", response_model=Article)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    """创建新文章"""
    # 这里应该添加实际的数据库操作
    return {
        "id": 1,
        "title": article.title,
        "content": article.content,
        "author_id": article.author_id,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }


@router.get("/", response_model=List[Article])
def list_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """获取文章列表"""
    # 这里应该添加实际的数据库操作
    return []


@router.get("/{article_id}", response_model=Article)
def get_article(article_id: int, db: Session = Depends(get_db)):
    """获取单篇文章"""
    # 这里应该添加实际的数据库操作
    return {
        "id": article_id,
        "title": "示例文章",
        "content": "这是文章内容",
        "author_id": 1,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    } 