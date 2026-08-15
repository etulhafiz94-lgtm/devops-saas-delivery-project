from app.main import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_get_tasks():
    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={"title": "Learn Docker"}
    )

    assert response.status_code == 201
    assert response.get_json()["title"] == "Learn Docker"


def test_delete_task():
    client = app.test_client()

    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Task deleted"}