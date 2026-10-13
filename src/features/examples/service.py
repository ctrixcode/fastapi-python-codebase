# src/features/examples/service.py
from collections.abc import Sequence

from .models import Example
from .repositories import IExampleRepository
from .schemas import ExampleCreate, ExampleUpdate


class ExampleService:
    """
    Business logic and service orchestration for the Example feature.
    Decoupled from any database engine via IExampleRepository.
    """

    def __init__(self, repository: IExampleRepository):
        self._repository = repository

    async def create_example(self, data: ExampleCreate) -> Example:
        entity = Example(
            name=data.name,
            description=data.description,
        )
        return await self._repository.create(entity)

    async def get_example(self, example_id: int) -> Example | None:
        return await self._repository.get_by_id(example_id)

    async def get_examples(self, skip: int = 0, limit: int = 100) -> Sequence[Example]:
        return await self._repository.list_examples(skip=skip, limit=limit)

    async def update_example(
        self, example_id: int, data: ExampleUpdate
    ) -> Example | None:
        update_data = data.model_dump(exclude_unset=True)
        return await self._repository.update(
            example_id=example_id, update_data=update_data
        )

    async def delete_example(self, example_id: int) -> bool:
        return await self._repository.delete(example_id)
