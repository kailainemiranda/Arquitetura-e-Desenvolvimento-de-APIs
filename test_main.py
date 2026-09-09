from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={"name": "Alice Code", "email": "alice@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice Code"
    assert "id" in data

def test_add_skill():
    student_res = client.post("/students/", json={"name": "Bob Algo", "email": "bob@example.com"})
    student_id = student_res.json()["id"]

    skill_res = client.post(f"/students/{student_id}/skills/", json={"subject": "python", "stability_factor": 7.0})
    assert skill_res.status_code == 200
    assert skill_res.json()["subject"] == "python"
    assert skill_res.json()["retention_score"] > 90.0
