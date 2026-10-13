import pytest

from src.features.examples.models import Example
from src.features.examples.repositories import PostgresExampleRepository
from tests.test_db import TestingSessionLocal


@pytest.mark.anyio(backend="asyncio")
async def test_example_repository_crud(create_test_tables):
    async with TestingSessionLocal() as session:
        repo = PostgresExampleRepository(session=session)

        # 1. Create
        entity = Example(
            name="Feature Repo Test", description="Testing feature repository"
        )
        created = await repo.create(entity)
        assert created.id is not None
        assert created.name == "Feature Repo Test"

        # 2. Get by ID
        fetched = await repo.get_by_id(created.id)
        assert fetched is not None
        assert fetched.id == created.id
        assert fetched.name == "Feature Repo Test"

        # 3. List
        items = await repo.list_examples(skip=0, limit=10)
        assert len(items) == 1
        assert items[0].id == created.id

        # 4. Update
        updated = await repo.update(
            created.id, {"name": "Updated Feature Repo Test", "description": "Modified"}
        )
        assert updated is not None
        assert updated.name == "Updated Feature Repo Test"
        assert updated.description == "Modified"

        # 5. Delete
        assert await repo.delete(created.id) is True
        assert await repo.get_by_id(created.id) is None
