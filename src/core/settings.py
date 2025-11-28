from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "FastAPI Python Codebase"
    app_version: str = "1.0.0"
    APP_ENV: str = "development"
    UVICORN_HOST: str = "127.0.0.1"
    UVICORN_PORT: int = 8000
    DATABASE_URL: str = "postgresql+asyncpg://user:password@host:port/db_name"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
