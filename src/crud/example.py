from typing import Sequence
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.example import Example
from src.schemas.example import ExampleCreate, ExampleUpdate


async def create_example(session: AsyncSession, example: ExampleCreate) -> Example:
    db_example = Example(**example.model_dump())
    session.add(db_example)
    await session.commit()
    await session.refresh(db_example)
    return db_example


async def get_example(session: AsyncSession, example_id: int) -> Example | None:
    return await session.get(Example, example_id)


async def get_examples(
    session: AsyncSession, skip: int = 0, limit: int = 100
) -> Sequence[Example]:
    result = await session.execute(select(Example).offset(skip).limit(limit))
    return result.scalars().all()


async def update_example(
    session: AsyncSession, example_id: int, example: ExampleUpdate
) -> Example | None:
    db_example = await session.get(Example, example_id)
    if db_example:
        for key, value in example.model_dump(exclude_unset=True).items():
            setattr(db_example, key, value)
        await session.commit()
        await session.refresh(db_example)
    return db_example


async def delete_example(session: AsyncSession, example_id: int) -> Example | None:
    db_example = await session.get(Example, example_id)
    if db_example:
        await session.delete(db_example)
        await session.commit()
    return db_example
