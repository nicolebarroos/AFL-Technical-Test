import pytest

from domain.entities.user import User

@pytest.fixture
def user():
    return User(email="test@example.com", password="securepassword123")

def test_create_user(user):
    assert user.email == "test@example.com"
    assert user.password != "securepassword123"
    assert len(user.password) > 0

def test_verify_password(user):
    assert user.verify_password("securepassword123") is True
    assert user.verify_password("wrongpassword") is False
