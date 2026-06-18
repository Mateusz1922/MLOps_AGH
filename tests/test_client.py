from fastapi.testclient import TestClient
from app import app  # Zakładamy, że obiekt FastAPI() znajduje się w pliku app.py

client = TestClient(app)


def test_welcome_root_endpoint():
    """Testuje trasę główną /"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check_endpoint():
    """Testuje trasę /health"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
