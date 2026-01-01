from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login():
    response = client.post("/api/v1/auth/login", data={"username": "test", "password": "password"})
    assert response.status_code == 200
 Jonah
 Jonah
 Jonah
