from functools import lru_cache
from typing import Any, Dict
from pydantic_settings import BaseSettings
import os
from pathlib import Path


class ConfigManager:
    """Configuration manager for handling environment variables"""
    
    def __init__(self):
        self.env_file = self._get_env_file()
        self.settings = self._load_settings()

    def _get_env_file(self) -> str:
        """Get the appropriate .env file based on environment"""
        env = os.getenv("APP_ENV", "local")
        env_file = f".env.{env}"
        
        if not Path(env_file).exists():
            env_file = ".env"
            
        return env_file

    def _load_settings(self) -> Dict[str, Any]:
        """Load settings from environment variables"""
        return {
            # Application
            "APP_NAME": os.getenv("APP_NAME", "Llama FastAPI"),
            "APP_ENV": os.getenv("APP_ENV", "local"),
            "APP_DEBUG": os.getenv("APP_DEBUG", "true").lower() == "true",
            "APP_URL": os.getenv("APP_URL", "http://localhost:8000"),
            "APP_KEY": os.getenv("APP_KEY", "base64:your-secret-key-here"),

            # Server
            "SERVER_HOST": os.getenv("SERVER_HOST", "0.0.0.0"),
            "SERVER_PORT": int(os.getenv("SERVER_PORT", "8000")),

            # Database
            "DB_CONNECTION": os.getenv("DB_CONNECTION", "postgresql"),
            "DB_HOST": os.getenv("DB_HOST", "localhost"),
            "DB_PORT": int(os.getenv("DB_PORT", "5432")),
            "DB_DATABASE": os.getenv("DB_DATABASE", "llama_fastapi"),
            "DB_USERNAME": os.getenv("DB_USERNAME", "postgres"),
            "DB_PASSWORD": os.getenv("DB_PASSWORD", "postgres"),

            # JWT
            "JWT_SECRET": os.getenv("JWT_SECRET", "your-jwt-secret-key-here"),
            "JWT_ALGORITHM": os.getenv("JWT_ALGORITHM", "HS256"),
            "JWT_ACCESS_TOKEN_EXPIRE_MINUTES": int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30")),

            # Mail
            "MAIL_MAILER": os.getenv("MAIL_MAILER", "smtp"),
            "MAIL_HOST": os.getenv("MAIL_HOST", "smtp.mailtrap.io"),
            "MAIL_PORT": int(os.getenv("MAIL_PORT", "2525")),
            "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
            "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD"),
            "MAIL_ENCRYPTION": os.getenv("MAIL_ENCRYPTION"),
            "MAIL_FROM_ADDRESS": os.getenv("MAIL_FROM_ADDRESS"),
            "MAIL_FROM_NAME": os.getenv("MAIL_FROM_NAME", "Llama FastAPI"),

            # Redis
            "REDIS_HOST": os.getenv("REDIS_HOST", "127.0.0.1"),
            "REDIS_PASSWORD": os.getenv("REDIS_PASSWORD"),
            "REDIS_PORT": int(os.getenv("REDIS_PORT", "6379")),

            # Cache
            "CACHE_DRIVER": os.getenv("CACHE_DRIVER", "file"),
            "CACHE_PREFIX": os.getenv("CACHE_PREFIX", "llama_cache"),

            # Session
            "SESSION_DRIVER": os.getenv("SESSION_DRIVER", "file"),
            "SESSION_LIFETIME": int(os.getenv("SESSION_LIFETIME", "120")),

            # Logging
            "LOG_CHANNEL": os.getenv("LOG_CHANNEL", "stack"),
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "debug"),
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value"""
        return self.settings.get(key, default)

    def all(self) -> Dict[str, Any]:
        """Get all configuration values"""
        return self.settings.copy()


@lru_cache()
def get_config() -> ConfigManager:
    """Get cached configuration manager instance"""
    return ConfigManager() 