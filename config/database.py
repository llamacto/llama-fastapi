import os
from sqlalchemy import create_engine
from config.config import settings

# Build the database URL from environment variables
DATABASE_URL = (
    f"{settings.POSTGRES_SERVER}://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}/{settings.POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL, echo=settings.DEBUG) 