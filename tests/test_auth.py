from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/auth/register", json={"username": "testuser", "password": "password"})
    assert response.status_code == 200
    assert response.json()["message"] == "Usuário registrado com sucesso"

def test_login_user():
    client.post("/auth/register", json={"username": "testuser2", "password": "password"})
    response = client.post("/auth/token", json={"username": "testuser2", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
