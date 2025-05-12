from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache
from .config_manager import get_config

config = get_config()


class Settings(BaseSettings):
    PROJECT_NAME: str = config.get("APP_NAME")
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DESCRIPTION: str = "Llama FastAPI Project"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"
    ALLOWED_ORIGINS: list = ["*"]
    
    # Database
    POSTGRES_SERVER: str = config.get("DB_HOST")
    POSTGRES_USER: str = config.get("DB_USERNAME")
    POSTGRES_PASSWORD: str = config.get("DB_PASSWORD")
    POSTGRES_DB: str = config.get("DB_DATABASE")
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    # JWT
    SECRET_KEY: str = config.get("JWT_SECRET")
    ALGORITHM: str = config.get("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config.get("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")

    # Server
    HOST: str = config.get("SERVER_HOST")
    PORT: int = config.get("SERVER_PORT")

    # Debug
    DEBUG: bool = config.get("APP_DEBUG")

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "allow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.SQLALCHEMY_DATABASE_URI:
            self.SQLALCHEMY_DATABASE_URI = (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
            )


@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings() 