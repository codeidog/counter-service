import os
import sys

import pytest

# Add the current directory to the Python path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the app, but we need to import it as a module
import importlib.util

spec = importlib.util.spec_from_file_location("counter_service", "counter-service.py")
counter_service = importlib.util.module_from_spec(spec)
spec.loader.exec_module(counter_service)

app = counter_service.app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_index(client):
    """Test that the GET index endpoint works."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Counter Dashboard" in response.data
    assert b"GET requests:" in response.data


def test_post_index(client):
    """Test that the POST index endpoint works."""
    response = client.post("/")
    assert response.status_code == 200
    assert b"Hmm, Plus 1 please" in response.data


def test_counter_increments(client):
    """Test that counters increment correctly."""
    # Reset counters by accessing the global variables
    counter_service.get_counter = 0
    counter_service.post_counter = 0

    # Test GET counter increment
    response = client.get("/")
    assert response.status_code == 200
    assert b"GET requests:</strong> 1" in response.data

    # Test POST counter increment
    response = client.post("/")
    assert response.status_code == 200

    # Check both counters after incrementing
    response = client.get("/")
    assert response.status_code == 200
    assert b"GET requests:</strong> 2" in response.data
    assert b"POST requests:</strong> 1" in response.data
