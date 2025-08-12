import uuid

BASE_EMAIL = "test_user_{}@test.com"
PASSWORD = "pas123"
NAME = "User Test"


def generate_random_email():
    """Генерирует уникальный email для тестов"""
    return f"test_user_{uuid.uuid4().hex[:8]}@test.com"

