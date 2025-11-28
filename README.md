# FastAPI Python Codebase Template

This project is a production-ready template for building modern, asynchronous web APIs with Python, FastAPI, and PostgreSQL. It's designed with a modular architecture, best practices, and a focus on developer experience.

## Features

- **Modern Tech Stack**: FastAPI, Python 3.11+, SQLModel (based on Pydantic and SQLAlchemy), and `asyncpg`.
- **Fully Asynchronous**: Async support from the database to the endpoint.
- **Production-Ready**: Structured logging, centralized settings management, and graceful shutdown.
- **Modular Architecture**: Organize your code by features, keeping it clean and scalable.
- **Dependency Management**: Uses `uv` for fast and reliable dependency management.
- **Database Integration**: Pre-configured with SQLModel for ORM and `asyncpg` for high-performance PostgreSQL communication. Tables are auto-generated on startup.
- **Code Quality**: Linting and formatting enforced by `ruff` and `pre-commit`.
- **Testing**: `pytest` setup with example tests.
- **API Client**: Includes a `bruno` collection for easy API testing.

## Getting Started

### Prerequisites

- Python 3.11 or later.
- `uv` package manager (`pip install uv`).
- A running PostgreSQL database instance.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate # On Windows, use `.\.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    The project uses `uv` for dependency management. Install all required packages, including testing tools:
    ```bash
    uv pip install -e ".[test]"
    ```

4.  **Configure environment variables:**
    Copy the example environment file and update it with your database credentials and other settings.
    ```bash
    cp .env.example .env
    ```
    Now, edit the `.env` file:
    ```env
    APP_ENV=development
    HOST=127.0.0.1
    PORT=8001
    DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/db_name"
    ```

### Running the Application

To run the application, use `uvicorn` directly. It will automatically pick up the `UVICORN_HOST` and `UVICORN_PORT` variables from your `.env` file.

1.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate # On Windows, use `.\.venv\Scripts\activate`
    ```

2.  **Run the development server:**
    This command starts the server with "hot-reloading", which automatically restarts the server when you make code changes.
    ```bash
    uv run uvicorn src.app:app --reload
    ```

The API will be available at the host and port specified in your `.env` file (e.g., `http://127.0.0.1:8001`).

### Running Tests

To run the test suite, use `pytest`:
```bash
pytest
```

## Project Structure

```
├── src/
│   ├── api/              # API versioning and routing
│   ├── core/             # Core components (DB, settings, logging)
│   ├── features/         # Business logic organized by feature
│   │   └── examples/     # An example CRUD feature
│   │       ├── api.py    # Endpoints
│   │       ├── crud.py   # Database operations
│   │       ├── model.py  # Database table model
│   │       └── schema.py # Pydantic schemas
│   ├── schemas/          # Global Pydantic schemas
│   └── app.py            # FastAPI app factory and root endpoint
├── tests/                # Application tests
├── .env.example          # Example environment variables
├── main.py               # Main application entrypoint
├── pyproject.toml        # Project metadata and dependencies
└── README.md
```

## API Endpoints

The template includes the following endpoints:

- **`GET /`**: Health check to confirm the API is running.
- **`POST /api/v1/examples/`**: Create a new example.
- **`GET /api/v1/examples/`**: Retrieve a list of examples.
- **`GET /api/v1/examples/{example_id}`**: Retrieve a single example by ID.
- **`PUT /api/v1/examples/{example_id}`**: Update an example.
- **`DELETE /api/v1/examples/{example_id}`**: Delete an example.

You can test these endpoints using the provided Bruno collection in the `bruno/` directory.
