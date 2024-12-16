import pytest
from fastapi.testclient import TestClient
from main import app  # Импортируйте ваше приложение FastAPI

client = TestClient(app)

@pytest.fixture
def setup_database():
    # Здесь вы можете подготовить вашу базу данных
    # Например, создать тестовые данные или очистить базу перед тестами
    yield
    # Здесь вы можете очистить базу данных после тестов, если это необходимо

def test_start(setup_database):
    response = client.post("/api-demka/start")
    assert response.status_code == 200
    assert response.json() == {"log": "базы созданы"}

def test_add_customer(setup_database):
    customer_data = {
        "id": 1,
        "name": "John Doe",
        "contact_info": "john@example.com",
        "address": "123 Main St"
    }
    response = client.post("/api-demka/add", json=customer_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Запись добавлена"}

def test_add_customer_missing_fields(setup_database):
    customer_data = {
        "name": "John Doe",
        "contact_info": "john@example.com"
        # Missing address
    }
    response = client.post("/api-demka/add", json=customer_data)
    assert response.status_code == 422  # Expecting a 422 error

def test_update_customer(setup_database):
    customer_data = {
        "id": 1,
        "name": "John Doe Updated",
        "contact_info": "john_updated@example.com",
        "address": "456 Main St"
    }
    response = client.post("/api-demka/update", json=customer_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Запись обновлена"}

def test_delete_customer(setup_database):
    # Ensure a customer exists first
    client.post("/api-demka/add", json={
        "id": 1,
        "name": "John Doe",
        "contact_info": "john@example.com",
        "address": "123 Main St"
    })
    
    customer_data = [
        {"id": 1}
    ]
    response = client.post("/api-demka/delete", json=customer_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Запись удалена"}  # Adjust according to your API response

def test_add_order(setup_database):
    order_data = {
        "id": 1,
        "order_data": "2024-12-13",
        "customer": "John Doe",
        "total_amount": 100.0
    }
    response = client.post("/api-demka/add1", json=order_data)
    assert response.status_code == 200
    assert "message" not in response.json()  # Убедитесь, что нет сообщения об ошибке

def test_update_order(setup_database):
    order_data = {
        "id": 1,
        "order_data": "2024-12-14",
        "customer": "John Doe Updated",
        "total_amount": 150.0
    }
    response = client.post("/api-demka/update1", json=order_data)
    assert response.status_code == 200
    assert "message" not in response.json()  # Убедитесь, что нет сообщения об ошибке

def test_delete_order(setup_database):
    order_data = [
        {"id": 1}
    ]
    response = client.post("/api-demka/delete1", json=order_data)
    assert response.status_code == 200
    assert "message" not in response.json()  # Убедитесь, что нет сообщения об ошибке