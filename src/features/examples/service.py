from typing import Sequence

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from .model import Example
from .schema import ExampleCreate, ExampleUpdate


class ExampleService:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def create_example(self, example_data: ExampleCreate) -> Example:
        db_example = Example.model_validate(example_data)
        self._db.add(db_example)
        await self._db.commit()
        await self._db.refresh(db_example)
        return db_example

    async def get_example(self, example_id: int) -> Example | None:
        return await self._db.get(Example, example_id)

    async def get_examples(self, skip: int = 0, limit: int = 100) -> Sequence[Example]:
        result = await self._db.execute(select(Example).offset(skip).limit(limit))
        return result.scalars().all()

    async def update_example(
        self, example_id: int, example_data: ExampleUpdate
    ) -> Example | None:
        db_example = await self.get_example(example_id)
        if not db_example:
            return None

        update_data = example_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_example, key, value)

        self._db.add(db_example)
        await self._db.commit()
        await self._db.refresh(db_example)
        return db_example

    async def delete_example(self, example_id: int) -> bool:
        db_example = await self.get_example(example_id)
        if not db_example:
            return False

        await self._db.delete(db_example)
        await self._db.commit()
        return True
