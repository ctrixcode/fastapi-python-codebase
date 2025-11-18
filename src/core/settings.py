from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Python Codebase"
    app_version: str = "1.0.0"
