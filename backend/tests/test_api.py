from fastapi.testclient import TestClient

from main import app
from app.api.dependencies import get_agent_orchestrator

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["docs"] == "/docs"


def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_validates_required_fields():
    app.dependency_overrides[get_agent_orchestrator] = lambda: object()
    try:
        response = client.post("/api/chat", json={"repository_id": "owner/repo"})
        assert response.status_code == 422
    finally:
        app.dependency_overrides.clear()
