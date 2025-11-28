from sqlmodel import Field, SQLModel


class Example(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
