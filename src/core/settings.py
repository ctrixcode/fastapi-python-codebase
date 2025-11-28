from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "FastAPI Python Codebase"
    app_version: str = "1.0.0"
    APP_ENV: str = "development"
    UVICORN_HOST: str = "127.0.0.1"
    UVICORN_PORT: int = 8000

    # Database credentials
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "user"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "db_name"

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        """
        Construct the database URL from components.
        """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
