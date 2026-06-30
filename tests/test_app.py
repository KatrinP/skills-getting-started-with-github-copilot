from fastapi.testclient import TestClient

from src import app as app_module

client = TestClient(app_module.app)


def test_unregister_participant_removes_email_from_activity():
    original_participants = app_module.activities["Chess Club"]["participants"].copy()

    try:
        response = client.delete(
            "/activities/Chess%20Club/signup?email=michael@mergington.edu"
        )

        assert response.status_code == 200
        assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"
        assert "michael@mergington.edu" not in app_module.activities["Chess Club"]["participants"]
    finally:
        app_module.activities["Chess Club"]["participants"] = original_participants
