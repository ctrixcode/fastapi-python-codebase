from typing import Sequence
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.database import get_db
from . import crud
from .schema import ExampleCreate, ExampleRead, ExampleUpdate

router = APIRouter()


@router.post("/", response_model=ExampleRead)
async def create_example(example: ExampleCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_example(session=db, example=example)


@router.get("/", response_model=Sequence[ExampleRead])
async def read_examples(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    return await crud.get_examples(session=db, skip=skip, limit=limit)


@router.get("/{example_id}", response_model=ExampleRead)
async def read_example(example_id: int, db: AsyncSession = Depends(get_db)):
    db_example = await crud.get_example(session=db, example_id=example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example


@router.put("/{example_id}", response_model=ExampleRead)
async def update_example(
    example_id: int, example: ExampleUpdate, db: AsyncSession = Depends(get_db)
):
    db_example = await crud.update_example(
        session=db, example_id=example_id, example=example
    )
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example


@router.delete("/{example_id}", response_model=ExampleRead)
async def delete_example(example_id: int, db: AsyncSession = Depends(get_db)):
    db_example = await crud.delete_example(session=db, example_id=example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example
