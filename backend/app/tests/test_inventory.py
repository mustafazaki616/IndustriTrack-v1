from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_inventory():
    response = client.get("/api/v1/inventory/")
    assert response.status_code == 200
