# src/features/examples/repositories/interface.py
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any

from ..models import Example


class IExampleRepository(ABC):
    """
    Abstract Repository Interface for Example persistence.
    Any database engine (PostgreSQL, MySQL, Redis, Mongo) must implement this contract.
    """

    @abstractmethod
    async def get_by_id(self, example_id: int) -> Example | None:
        """Retrieve an example by unique identifier."""
        ...

    @abstractmethod
    async def list_examples(self, skip: int = 0, limit: int = 100) -> Sequence[Example]:
        """Retrieve a list of examples."""
        ...

    @abstractmethod
    async def create(self, example: Example) -> Example:
        """Persist a new example entity."""
        ...

    @abstractmethod
    async def update(
        self, example_id: int, update_data: dict[str, Any]
    ) -> Example | None:
        """Update an existing example entity."""
        ...

    @abstractmethod
    async def delete(self, example_id: int) -> bool:
        """Delete an example by unique identifier."""
        ...
