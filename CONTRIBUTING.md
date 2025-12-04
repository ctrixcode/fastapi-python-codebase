# Contributing to the FastAPI Codebase Template

First off, thank you for considering contributing! Your help is essential for keeping this project great.

## How to Contribute

- **Reporting Bugs**: If you find a bug, please open an issue and provide a clear description, steps to reproduce it, and the expected behavior.
- **Suggesting Enhancements**: If you have an idea for a new feature or an improvement, open an issue to discuss it. This lets us coordinate our efforts and prevent duplication of work.
- **Pull Requests**: If you're ready to contribute code, please submit a pull request.

## Development Setup

Follow the setup instructions in the `README.md` to get your local development environment up and running. A quick summary:

1.  Clone the repo.
2.  Create and activate a virtual environment: `python -m venv .venv && source .venv/bin/activate`.
3.  Install dependencies: `uv pip install -e ".[test]"`.
4.  Set up your `.env` file from `.env.example`.
5.  Run the development server: `uvicorn src.app:app --reload --host 127.0.0.1 --port 8001`.

## Coding Standards

To maintain code quality and consistency, we use `ruff` for formatting and linting.

- **Formatting**: Before committing, please format your code:
  ```bash
  ruff format .
  ```
- **Linting**: Check for any linting errors:
  ```bash
  ruff check .
  ```

This project also uses `pre-commit` hooks to automatically run these checks before you commit. To set it up, run:
```bash
pre-commit install
```

## Adding a New Feature

This project is designed to be modular. To add a new feature (e.g., "products"), follow these steps:

1.  **Define the Database Model (`src/models/product.py`):**
    Create a `Product` class that inherits from `SQLModel`. This will be your database table schema.

    ```python
    # src/models/product.py
    from sqlmodel import Field, SQLModel

    class Product(SQLModel, table=True):
        id: int = Field(default=None, primary_key=True)
        name: str
        price: float
    ```

2.  **Define Pydantic Schemas (`src/schemas/product.py`):**
    Create schemas for creating, reading, and updating the resource. This ensures data validation.

    ```python
    # src/schemas/product.py
    from pydantic import BaseModel

    class ProductBase(BaseModel):
        name: str
        price: float

    class ProductCreate(ProductBase):
        pass

    class ProductRead(ProductBase):
        id: int

    class ProductUpdate(BaseModel):
        name: str | None = None
        price: float | None = None
    ```

3.  **Implement the Service (`src/services/product.py`):**
    Write the `ProductService` class with methods that interact with the database (Create, Read, Update, Delete).

4.  **Create the API Router (`src/api/v1/products.py`):**
    Define the API endpoints for your feature using an `APIRouter`.

5.  **Include the new router in the main API:**
    In `src/api/v1/api.py`, import and include your new router.

    ```python
    # src/api/v1/api.py
    from fastapi import APIRouter
    from src.api.v1.examples import router as example_router
    from src.api.v1.products import router as products_router # Add this

    api_router = APIRouter()
    api_router.include_router(example_router, prefix="/examples", tags=["examples"])
    api_router.include_router(products_router, prefix="/products", tags=["products"]) # Add this
    ```

6.  **Add Tests:**
    Create new test files in the `tests/` directory that mirror the `src` structure (e.g., `tests/api/test_products.py`, `tests/services/test_products.py`).

By following this structure, you help keep the codebase organized and easy to maintain. Thank you for your contribution!
