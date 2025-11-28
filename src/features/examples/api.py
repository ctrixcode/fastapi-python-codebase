from typing import Sequence

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.database import get_db
from src.core.exceptions import NotFoundException
from .schema import ExampleCreate, ExampleRead, ExampleUpdate
from .service import ExampleService

router = APIRouter()


# Dependency to provide the service
def get_example_service(db: AsyncSession = Depends(get_db)) -> ExampleService:
    return ExampleService(session=db)


@router.post("/", response_model=ExampleRead)
async def create_example(
    example: ExampleCreate, service: ExampleService = Depends(get_example_service)
):
    return await service.create_example(example_data=example)


@router.get("/", response_model=Sequence[ExampleRead])
async def read_examples(
    skip: int = 0,
    limit: int = 100,
    service: ExampleService = Depends(get_example_service),
):
    return await service.get_examples(skip=skip, limit=limit)


@router.get("/{example_id}", response_model=ExampleRead)
async def read_example(
    example_id: int, service: ExampleService = Depends(get_example_service)
):
    db_example = await service.get_example(example_id=example_id)
    if db_example is None:
        raise NotFoundException("Example not found")
    return db_example


@router.put("/{example_id}", response_model=ExampleRead)
async def update_example(
    example_id: int,
    example: ExampleUpdate,
    service: ExampleService = Depends(get_example_service),
):
    db_example = await service.update_example(
        example_id=example_id, example_data=example
    )
    if db_example is None:
        raise NotFoundException("Example not found")
    return db_example


@router.delete("/{example_id}")
async def delete_example(
    example_id: int, service: ExampleService = Depends(get_example_service)
):
    success = await service.delete_example(example_id=example_id)
    if not success:
        raise NotFoundException("Example not found")
    return {"ok": True}
