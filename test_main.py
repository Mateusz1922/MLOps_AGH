from fastapi.testclient import TestClient

# Importujemy obiekt app z Twojego pliku app.py
from app import app

# Tworzymy klienta testowego, który pozwala "wywoływać" endpointy bez uruchamiania uvicorna
client = TestClient(app)


def test_welcome_root():
    """Testuje czy endpoint główny (/) zwraca poprawną wiadomość powitalną."""
    response = client.get("/")

    # Sprawdzamy czy kod statusu HTTP to 200 (OK)
    assert response.status_code == 200
    # Sprawdzamy czy struktura JSON jest dokładnie taka, jakiej oczekujemy
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    """Testuje czy endpoint /health poprawnie zwraca status aplikacji."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
