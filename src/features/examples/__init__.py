# src/features/examples/__init__.py
from .models import Example
from .repositories import IExampleRepository, PostgresExampleRepository
from .router import router
from .schemas import ExampleCreate, ExampleRead, ExampleUpdate
from .service import ExampleService

__all__ = [
    "Example",
    "ExampleCreate",
    "ExampleRead",
    "ExampleService",
    "ExampleUpdate",
    "IExampleRepository",
    "PostgresExampleRepository",
    "router",
]
