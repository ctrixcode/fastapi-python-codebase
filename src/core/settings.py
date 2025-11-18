from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "FastAPI Python Codebase"
    app_version: str = "1.0.0"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
