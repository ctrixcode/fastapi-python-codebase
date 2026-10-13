# FastAPI Python Codebase Template

This project is a production-ready template for building modern, asynchronous web APIs with Python, FastAPI, and PostgreSQL. It is designed with **Feature-Based Architecture**, best practices, and a focus on developer experience.

## Features

- **Modern Tech Stack**: FastAPI, Python 3.11+, SQLModel (Pydantic + SQLAlchemy), and `asyncpg`.
- **Fully Asynchronous**: Async support from the database to the endpoint.
- **Production-Ready**: Structured logging, centralized settings management, and graceful shutdown.
- **Feature-Based Architecture**: Organize code by business capabilities, keeping all models, schemas, repositories, and routes co-located.
- **Fast Tooling & Package Management**: Uses **`uv`** exclusively for instant virtual environments, dependency resolution, and task execution.
- **Pluggable Persistence**: Decoupled repository interfaces supporting PostgreSQL, with readiness for multi-database extensions.
- **Code Quality**: Linting and formatting enforced by `ruff` and `pre-commit`.
- **Testing**: `pytest` setup with asynchronous in-memory SQLite isolation.
- **API Client**: Includes a `bruno` collection for easy API testing.

---

## Getting Started

### Prerequisites

- Python 3.11 or later.
- **`uv`** package manager (Install via `pip install uv` or official standalone installer: `curl -LsSf https://astral.sh/uv/install.sh | sh` / Windows PowerShell: `irm https://astral.sh/uv/install.ps1 | iex`).
- A running PostgreSQL database instance (or Docker).

---

### Installation & Virtual Environment Setup with `uv`

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd fastapi-python-codebase
   ```

2. **Create a virtual environment with `uv`:**
   ```bash
   uv venv
   ```
   *(To target a specific Python version, run `uv venv --python 3.11`)*

3. **Activate the virtual environment:**

   - **On Windows (PowerShell):**
     ```powershell
     .venv\Scripts\activate
     ```
   - **On Windows (Command Prompt):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **On Linux / macOS (Bash / Zsh):**
     ```bash
     source .venv/bin/activate
     ```

4. **Install & synchronize all dependencies:**
   ```bash
   uv sync
   ```

> [!TIP]
> **Pro Tip:** With `uv`, you don't even need to manually activate the virtual environment! You can prepend any command with `uv run`, and `uv` will automatically execute it within your project's `.venv`:
> ```bash
> uv run pytest
> uv run uvicorn src.app:app --reload
> ```

---

### Environment Configuration

Copy the example environment file and configure your database credentials:

```bash
cp .env.example .env
```

Edit your `.env` file:
```env
APP_ENV=development
UVICORN_HOST=127.0.0.1
UVICORN_PORT=8000

# Database Credentials
DB_HOST=localhost
DB_PORT=5432
DB_USER=user
DB_PASSWORD=password
DB_NAME=db_name
```

---

### Running the Application

Start the development server with live auto-reloading:

```bash
uv run uvicorn src.app:app --host 127.0.0.1 --port 8000 --reload
```

The API interactive documentation will be available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### Running Tests & Code Quality

Run tests using `pytest`:
```bash
uv run pytest
```

Check and format code with `ruff`:
```bash
uv run ruff check
uv run ruff format
```

---

## Project Structure

The project follows a **Feature-Based Architecture**:

```text
fastapi-python-codebase/
├── src/
│   ├── app.py                       # Application factory, lifespan, and root endpoint
│   ├── api/                         # Global API versioning & router mounting
│   │   └── v1/
│   │       └── api.py               # Aggregates feature routers
│   ├── core/                        # Global core infrastructure
│   │   ├── database.py              # Async PostgreSQL engine and session factory
│   │   ├── exceptions.py            # Global custom exceptions
│   │   ├── logger.py                # Structured logging configuration
│   │   ├── messages.py              # Centralized message strings
│   │   ├── settings.py              # Pydantic BaseSettings environment loader
│   │   └── utils.py                 # Common utility functions
│   ├── schemas/                     # Global / shared schemas (health, response envelope)
│   └── features/                    # Business features (Vertical slices)
│       └── examples/                # Example feature package
│           ├── models.py            # SQLModel table definition
│           ├── schemas.py           # Feature Pydantic request/response schemas
│           ├── repositories/        # Persistence layer
│           │   ├── interface.py     # Abstract IExampleRepository contract
│           │   ├── postgres.py      # Concrete PostgreSQL implementation
│           │   └── __init__.py
│           ├── service.py           # Feature business logic orchestration
│           ├── router.py            # FastAPI endpoints & dependency injection
│           └── __init__.py
├── tests/                           # Isolated test suites
│   ├── api/                         # End-to-end API HTTP tests
│   ├── features/                    # Feature repository & service tests
│   ├── test_db.py                   # In-memory SQLite async test database setup
│   └── conftest.py
├── .vscode/
│   └── settings.json                # Project settings (hiding cache folders)
├── .env.example
├── pyproject.toml
└── uv.lock
```

---

## API Endpoints

The baseline template includes:

- **`GET /`**: Health check to confirm API status.
- **`POST /api/v1/examples/`**: Create a new example.
- **`GET /api/v1/examples/`**: Retrieve a list of examples.
- **`GET /api/v1/examples/{example_id}`**: Retrieve a single example by ID.
- **`PUT /api/v1/examples/{example_id}`**: Update an existing example.
- **`DELETE /api/v1/examples/{example_id}`**: Delete an example.

You can also test these endpoints using the provided Bruno collection in the `bruno/` directory.
