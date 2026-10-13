# src/features/examples/router.py
from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.database import get_db
from src.core.exceptions import NotFoundException

from .models import Example
from .repository import ExampleRepository
from .schemas import ExampleCreate, ExampleRead, ExampleUpdate
from .service import ExampleService

router = APIRouter()


def get_example_repository(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> ExampleRepository:
    return ExampleRepository(session=db)


def get_example_service(
    repo: Annotated[ExampleRepository, Depends(get_example_repository)],
) -> ExampleService:
    return ExampleService(repository=repo)


ExampleServiceDep = Annotated[ExampleService, Depends(get_example_service)]


@router.post("/", response_model=ExampleRead)
async def create_example(
    example: ExampleCreate,
    service: ExampleServiceDep,
) -> Example:
    return await service.create_example(data=example)


@router.get("/", response_model=Sequence[ExampleRead])
async def read_examples(
    service: ExampleServiceDep,
    skip: int = 0,
    limit: int = 100,
) -> Sequence[Example]:
    return await service.get_examples(skip=skip, limit=limit)


@router.get("/{example_id}", response_model=ExampleRead)
async def read_example(
    example_id: int,
    service: ExampleServiceDep,
) -> Example:
    db_example = await service.get_example(example_id=example_id)
    if db_example is None:
        raise NotFoundException("Example not found")
    return db_example


@router.put("/{example_id}", response_model=ExampleRead)
async def update_example(
    example_id: int,
    example: ExampleUpdate,
    service: ExampleServiceDep,
) -> Example:
    db_example = await service.update_example(example_id=example_id, data=example)
    if db_example is None:
        raise NotFoundException("Example not found")
    return db_example


@router.delete("/{example_id}")
async def delete_example(
    example_id: int,
    service: ExampleServiceDep,
) -> dict[str, bool]:
    success = await service.delete_example(example_id=example_id)
    if not success:
        raise NotFoundException("Example not found")
    return {"ok": True}
