from pydantic import BaseModel


class ExampleBase(BaseModel):
    name: str
    description: str


class ExampleCreate(ExampleBase):
    pass


class ExampleRead(ExampleBase):
    id: int


class ExampleUpdate(ExampleBase):
    pass
