import requests
from urls import Url
import allure

class UserApi:
    @staticmethod
    @allure.step("Запрс на Создание пользователя")
    def create_user(payload):
        return requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", json=payload)

    @staticmethod
    @allure.step("Запрс на Авторизацию пользователя")
    def login_user(email, password):
        payload = {
        "email": email,
        "password": password
    }

        return requests.post(
            f"{Url.BASE_URL}{Url.LOGIN_USER}",
            json=payload
    )

    @staticmethod
    @allure.step("Запрс на Удаление пользователя")
    def delete_user(token):
        headers = {
            "Authorization": token
        }
        return requests.delete(
            f"{Url.BASE_URL}{Url.DELETE_USER}", headers=headers
        )
    
