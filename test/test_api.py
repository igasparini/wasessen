from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_recipe():
    response = client.get("/recipe?time=30&calories=500&keywords=pasta")
    assert response.status_code == 200
    assert response.json() is not None
    # Add more assertions based on your expected JSON response