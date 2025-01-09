from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_image():
    with open("tests/test_image.jpg", "rb") as img:
        response = client.post("/api/upload/", files={"file": ("test_image.jpg", img, "image/jpeg")})
    assert response.status_code == 200
    assert "objects_detected" in response.json()
