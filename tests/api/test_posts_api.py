import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_post():

    payload = {
        "title": "QA Automation Test",
        "body": "Testing API creation",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_delete_post():

    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200