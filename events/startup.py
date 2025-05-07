from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def startup_event(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        create_tables() 