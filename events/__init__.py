from fastapi import FastAPI
from typing import Callable
from sqlalchemy import text
from database.session import SessionLocal

def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        # Initialize database connection
        try:
            db = SessionLocal()
            await db.execute(text("SELECT 1"))
        except Exception as e:
            print(f"Database connection failed: {e}")
        finally:
            await db.close()

    return start_app

def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        # Clean up resources
        pass

    return stop_app
