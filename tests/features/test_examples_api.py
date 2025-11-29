import pytest
from fastapi.testclient import TestClient

from src.app import app
from src.features.examples.api import get_example_service
from src.features.examples.service import ExampleService
from tests.test_db import TestingSessionLocal


# Async generator for the overridden dependency
async def override_get_example_service():
    """
    Dependency override to use the test database session.
    """
    async with TestingSessionLocal() as session:
        yield ExampleService(session=session)


# Apply the override to the app
app.dependency_overrides[get_example_service] = override_get_example_service


@pytest.fixture(scope="module")
def client():
    """
    Pytest fixture to provide a TestClient instance for the tests.
    """
    with TestClient(app) as c:
        yield c


@pytest.mark.anyio(backend='asyncio')
async def test_create_and_get_example(client: TestClient, create_test_tables):
    """
    Tests creating an example and then retrieving it.
    The 'create_test_tables' fixture is explicitly requested to set up the DB.
    """
    # 1. Create a new example
    create_response = client.post(
        "/api/v1/examples/",
        json={"name": "Test Example", "description": "A test description"},
    )
    assert create_response.status_code == 200
    created_example = create_response.json()
    assert created_example["name"] == "Test Example"
    assert created_example["description"] == "A test description"
    assert "id" in created_example

    # 2. Fetch the same example by its ID
    example_id = created_example["id"]
    get_response = client.get(f"/api/v1/examples/{example_id}")
    assert get_response.status_code == 200
    fetched_example = get_response.json()
    assert fetched_example["id"] == example_id
    assert fetched_example["name"] == "Test Example"


@pytest.mark.anyio(backend='asyncio')
async def test_get_nonexistent_example(client: TestClient, create_test_tables):
    """
    Tests that fetching a nonexistent example returns a 404 error.
    The 'create_test_tables' fixture is explicitly requested to set up the DB.
    """
    response = client.get("/api/v1/examples/99999")
    assert response.status_code == 404
    assert response.json()["message"] == "Example not found"