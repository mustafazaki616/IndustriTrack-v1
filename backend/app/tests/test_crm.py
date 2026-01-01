from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_crm():
    response = client.get("/api/v1/crm/customers")
    assert response.status_code == 200
 Jonah
