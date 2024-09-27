from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/status")
def read_status():
    return {"status": "running"}

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}
