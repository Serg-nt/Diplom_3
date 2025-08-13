import uuid

def generate_random_email():
    """Генерирует уникальный email для тестов"""
    return f"test_user_{uuid.uuid4().hex[:8]}@test.com"