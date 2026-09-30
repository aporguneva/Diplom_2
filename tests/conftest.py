import pytest
from api_methods.user_api import UserApi
from helpers.helper import generate_user_data, get_access_token


#Фикстура удаления пользователей после теста 
@pytest.fixture
def cleanup_user():
    created_tokens = []
    yield created_tokens
    for token in created_tokens:
        if token:
            UserApi.delete_user(token)

#Фикстура создает и удаляет пользователя.
@pytest.fixture
def new_user(cleanup_user): #создаем унникального пользователя, а затем удаляем
    payload = generate_user_data()
    response = UserApi.create_user(payload)

    token = None

    if response.status_code == 200:
        token = get_access_token(response)
        cleanup_user.append(token)
    
    yield {
        "payload": payload,
        "token": token,
    }


#Фикстура регистрирует, авторизует и удаляет пользователя.
@pytest.fixture
def login_user(new_user):
    payload = new_user["payload"]

    login_response = UserApi.login_user(
        payload["email"],
        payload["password"]
    )

    access_token = None

    if login_response.status_code == 200:
        access_token = get_access_token(login_response)

        return {
        "email": payload["email"],
        "password": payload["password"],
        "access_token": access_token,
        "user_data": payload
        }
