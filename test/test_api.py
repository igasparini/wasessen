import sys
sys.path.insert(0, '..')
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_recipe():
    response = client.get("/api/recipe", params={"cooking_time": 30, "calories": 500, "keywords": "chicken"})
    assert response.status_code == 200

def test_signup():
    response = client.post("/api/signup", json={"email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json() == {"message": "Check your email for the confirmation link"}

def test_login():
    response = client.post("/api/login", json={"email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200