import pytest
from fastapi.testclient import TestClient
from src.main import app
import uuid

client = TestClient(app)

def generate_email():
    return f"test_{uuid.uuid4().hex}@example.com"

def test_register_user_success():
    email = generate_email()
    response = client.post("/auth/register", json={"email": email, "password": "securepassword"})

    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    assert data["email"]
    assert "created_at" in data

def test_register_user_email_in_use():
    email = generate_email()

    first = client.post("/auth/register", json={"email": email, "password": "123456"})
    assert first.status_code == 200

    second = client.post("/auth/register", json={"email": email, "password": "123456"})
    assert second.status_code == 400
    assert second.json()["detail"] == "Email já cadastrado"

def test_login_success():
    email = generate_email()
    client.post("/auth/register", json={"email": email, "password": "123456"})

    login = client.post("/auth/login", json={"email": email, "password": "123456"})
    assert login.status_code == 200, login.text

    token_data = login.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"

def test_login_invalid_credentials():
    resp = client.post("/auth/login", json={"email": "nope@example.com", "password": "wrong"})
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid credentials"
