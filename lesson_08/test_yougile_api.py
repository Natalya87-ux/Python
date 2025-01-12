import requests
import pytest


login 

# URL API
BASE_URL = "https://ru.yougile.com/api-v2"

# Тестовые данные
PROJECT_DATA = {
    "name": "Test Project",
    "description": "This is a test project."
}

INVALID_PROJECT_DATA = {
    "name": "",  # Поле обязательно
    "description": "This should fail due to missing name."
}

# Аутентификация (если требуется, добавьте ваш токен или необходимый заголовок)
HEADERS = {
    # 'Authorization': 'Bearer YOUR_API_TOKEN', # Раскомментируйте и добавьте ваш токен
    'Content-Type': 'application/json'
}

# Позитивные тесты
def test_create_project():
    response = requests.post(f"{BASE_URL}/projects", json=PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 201  # Ожидаем статус 201 Created
    assert "id" in response.json()  # Проверяем, что есть ID проекта

def test_get_projects():
    response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
    assert response.status_code == 200  # Ожидаем статус 200 OK
    assert isinstance(response.json(), list)  # Ожидаем, что ответ - это список

def test_update_project():
    project_id = 1  # Замените на актуальный ID проекта для тестирования
    update_data = {
        "name": "Updated Project",
        "description": "This project has been updated."
    }
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 200  # Ожидаем статус 200 OK
    assert response.json()['name'] == "Updated Project"  # Проверяем обновленное имя

def test_get_specific_project():
    project_id = 1  # Замените на актуальный ID проекта для тестирования
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200  # Ожидаем статус 200 OK
    assert response.json()['id'] == project_id  # Проверяем ID проекта

# Негативные тесты
def test_create_project_missing_name():
    response = requests.post(f"{BASE_URL}/projects", json=INVALID_PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 400  # Ожидаем статус 400 Bad Request
    assert "name" in response.json()['errors']  # Проверяем наличие ошибки по полю name

# Запуск тестов
if __name__ == "__main__":
    pytest.main()


### Запуск тестов

Сохраняем файл и запускаем тесты из командной строки:
bash
pytest test_yougile_api.py
`