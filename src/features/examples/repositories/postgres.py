# src/features/examples/repositories/postgres.py
from collections.abc import Sequence
from typing import Any

from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..models import Example
from .interface import IExampleRepository


class PostgresExampleRepository(IExampleRepository):
    """
    Concrete PostgreSQL repository implementation using SQLAlchemy / SQLModel AsyncSession.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, example_id: int) -> Example | None:
        stmt = select(Example).where(Example.id == example_id)
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def list_examples(self, skip: int = 0, limit: int = 100) -> Sequence[Example]:
        stmt = select(Example).offset(skip).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, example: Example) -> Example:
        self.session.add(example)
        await self.session.commit()
        await self.session.refresh(example)
        return example

    async def update(
        self, example_id: int, update_data: dict[str, Any]
    ) -> Example | None:
        stmt = select(Example).where(Example.id == example_id)
        result = await self.session.execute(stmt)
        model = result.scalars().first()
        if not model:
            return None

        for key, value in update_data.items():
            setattr(model, key, value)

        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model

    async def delete(self, example_id: int) -> bool:
        stmt = select(Example).where(Example.id == example_id)
        result = await self.session.execute(stmt)
        model = result.scalars().first()
        if not model:
            return False

        await self.session.delete(model)
        await self.session.commit()
        return True
