import pytest
from sqlmodel import SQLModel

# Note the absolute import path
from tests.test_db import engine


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def create_test_tables():
    """
    Fixture to create all tables in the test database before any tests run.
    This is in conftest.py to ensure it's set up before any tests are collected.
    """
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
