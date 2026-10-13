# src/features/examples/models.py
from sqlmodel import Field, SQLModel


class Example(SQLModel, table=True):
    """
    SQLModel table representation for the Example entity.
    Serves as both the database schema and domain model.
    """

    __tablename__ = "examples"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
