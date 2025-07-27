from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}

def test_read_search():
    response = client.get("/search/Barack%20Obama")
    assert response.status_code == 200
    assert "Barack Obama" in response.json()["result"]

def test_read_phrase():
    response = client.get("/phrase/Barack%20Obama")
    assert response.status_code == 200
    assert "american politician" in response.json()["result"]