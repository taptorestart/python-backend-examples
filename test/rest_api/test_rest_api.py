import requests
from dotenv import dotenv_values

BASE_URL = dotenv_values(".env")["BASE_URL"]
ADMIN_EMAIL = dotenv_values(".env")["ADMIN_EMAIL"]
ADMIN_PASSWORD = dotenv_values(".env")["ADMIN_PASSWORD"]


def test_get_index():
    """
    Test http://localhost:8000
    """
    endpoint = f"{BASE_URL}"
    response = requests.get(endpoint)
    assert response.status_code == 404


def test_get_docs():
    """
    Test http://localhost:8000/docs/
    """
    endpoint = f"{BASE_URL}/docs/"
    response = requests.get(endpoint)
    assert response.status_code == 200


def _get_admin_access_token():
    data = {
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    }
    endpoint = f"{BASE_URL}/api/v1/login/access-token"
    response = requests.post(url=endpoint, json=data)
    access_token = response.json()["access_token"]
    return access_token


def _get_headers_with_admin_access_token():
    access_token = _get_admin_access_token()
    headers = {
        "Content-type": "application/json",
        "Authorization": f"bearer {access_token}"
    }
    return headers


def test_get_api_v1_users_me():
    headers = _get_headers_with_admin_access_token()
    endpoint = f"{BASE_URL}/api/v1/users/me"
    response = requests.get(url=endpoint, headers=headers)
    assert response.json()["email"] == "taptorestart@gmail.com"


TEST_USER_EMAIL = "janedoe@gmail.com"
TEST_USER_PASSWORD = "verysecret"


def _register_test_user():
    headers = _get_headers_with_admin_access_token()
    endpoint = f"{BASE_URL}/api/v1/register"
    data = {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
    }
    requests.post(url=endpoint, headers=headers, json=data)
    return None


def _get_headers_with_test_user_access_token():
    _register_test_user()
    data = {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
    }
    endpoint = f"{BASE_URL}/api/v1/login/access-token"
    response = requests.post(url=endpoint, json=data)
    access_token = response.json()["access_token"]
    headers = {
        "Content-type": "application/json",
        "Authorization": f"bearer {access_token}"
    }
    return headers


def _get_test_user_id():
    headers = _get_headers_with_test_user_access_token()
    endpoint = f"{BASE_URL}/api/v1/users/me"
    response = requests.get(url=endpoint, headers=headers)
    user_id = response.json()["id"]
    return user_id


def test_patch_api_v1_users_id_by_admin():
    headers = _get_headers_with_admin_access_token()
    test_user_id = _get_test_user_id()
    endpoint = f"{BASE_URL}/api/v1/users/{test_user_id}"
    data = {
        "email": "johndoe@gmail.com"
    }
    response = requests.patch(url=endpoint, headers=headers, json=data)
    assert response.json()["email"] == "johndoe@gmail.com"
