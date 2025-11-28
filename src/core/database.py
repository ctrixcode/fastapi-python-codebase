from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel

from .settings import get_settings
from .logger import log

settings = get_settings()

async_engine = create_async_engine(settings.DATABASE_URL)


async def init_db():
    """
    Initializes the database and creates tables based on SQLModel metadata.
    """
    log.info("Attempting to initialize database and create tables...")
    async with async_engine.begin() as conn:
        # This command creates all tables that inherit from SQLModel.
        # It is idempotent, meaning it won't recreate tables that already exist.
        await conn.run_sync(SQLModel.metadata.create_all)
    log.info("Database tables created successfully (if they didn't exist).")


async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db():
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            log.error(e)
            raise e
        finally:
            await session.close()
