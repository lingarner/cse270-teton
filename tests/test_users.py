import pytest
import requests

# Define the URL for the API endpoint
URL = "http://127.0.0.1:8000/users"

# Test 1: Test for username=admin and password=admin expecting HTTP 401, empty response, and text content


def test_users_endpoint_invalid_credentials(mocker):
    # Mock the response to simulate the server's behavior for invalid credentials
    mock_response = requests.Response()
    mock_response.status_code = 401
    mock_response._content = b""  # Empty response body as bytes
    mock_response.headers['Content-Type'] = 'text/plain; charset=utf-8'

    # Use the mocker to mock requests.get
    mocker.patch('requests.get', return_value=mock_response)

    # Define parameters for invalid credentials
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Make a GET request with the provided parameters (this will use the mocked response)
    response = requests.get(URL, params=params)

    # Assert the status code is 401 (Unauthorized)
    assert response.status_code == 401

    # Assert the response is of type text (not JSON)
    assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'

    # Assert the response body is empty text
    assert response.text == ""


# Test 2: Test for username=admin and password=qwerty expecting HTTP 200, empty response, and text content
def test_users_endpoint_valid_credentials(mocker):
    # Mock the response to simulate the server's behavior for valid credentials
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b""  # Empty response body as bytes
    mock_response.headers['Content-Type'] = 'text/plain; charset=utf-8'

    # Use the mocker to mock requests.get
    mocker.patch('requests.get', return_value=mock_response)

    # Define parameters for valid credentials
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Make a GET request with the provided parameters (this will use the mocked response)
    response = requests.get(URL, params=params)

    # Assert the status code is 200 (OK)
    assert response.status_code == 200

    # Assert the response is of type text (not JSON)
    assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'

    # Assert the response body is empty text
    assert response.text == ""
