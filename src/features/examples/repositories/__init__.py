# src/features/examples/repositories/__init__.py
from .interface import IExampleRepository
from .postgres import PostgresExampleRepository

__all__ = ["IExampleRepository", "PostgresExampleRepository"]
