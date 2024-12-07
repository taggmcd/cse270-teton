import pytest
import requests
from unittest.mock import Mock

BASE_URL = "http://127.0.0.1:8000/users"

@pytest.fixture
def mock_requests_get(mocker):
    """Fixture to mock requests.get."""
    return mocker.patch("requests.get")

def test_users_endpoint_unauthorized(mock_requests_get):
    # Mock the server response for unauthorized request
    mock_response = Mock()
    mock_response.text = ""
    mock_response.status_code = 401
    mock_requests_get.return_value = mock_response

    # Define the URL and parameters
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Send the GET request
    response = requests.get(BASE_URL, params=params)

    # Assert that the response is empty
    assert response.text == "", "Expected an empty response"

    # Assert that the response status code is 401
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"

    # Verify the request was made with correct parameters
    mock_requests_get.assert_called_once_with(BASE_URL, params=params)


def test_users_endpoint_authorized(mock_requests_get):
    # Mock the server response for authorized request
    mock_response = Mock()
    mock_response.text = ""
    mock_response.status_code = 200
    mock_requests_get.return_value = mock_response

    # Define the URL and parameters
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Send the GET request
    response = requests.get(BASE_URL, params=params)

    # Assert that the response is empty
    assert response.text == "", "Expected an empty response"

    # Assert that the response status code is 200
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Verify the request was made with correct parameters
    mock_requests_get.assert_called_once_with(BASE_URL, params=params)
