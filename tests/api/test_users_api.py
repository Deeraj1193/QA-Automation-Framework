import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users():

    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    users = response.json()

    assert isinstance(users, list)

    assert len(users) > 0


def test_get_single_user():

    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1

    assert "username" in user