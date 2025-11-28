import pytest
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from src.features.examples.model import Example  # Import a model to get metadata

# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# Create an async engine
engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}, 
    echo=False,
)

# Create a sessionmaker for testing
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,  # Use AsyncSession
    expire_on_commit=False,
)


@pytest.fixture(scope="session", autouse=True)
async def create_test_tables():
    """
    Fixture to create all tables in the test database before any tests run.
    """
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
