from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_production():
    response = client.get("/api/v1/production/orders")
    assert response.status_code == 200
