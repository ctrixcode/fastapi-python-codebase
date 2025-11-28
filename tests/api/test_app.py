from fastapi.testclient import TestClient
from src.app import app  # Import the app from src/app.py

client = TestClient(app)


def test_root_endpoint():
    """
    Tests if the root endpoint ("/") returns a 200 OK status and the expected JSON.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"success": True, "data": {"message": "API is running."}}
