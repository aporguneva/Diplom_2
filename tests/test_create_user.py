import allure
from faker import Faker
from api_methods.user_api import UserApi
from data.data import ResponseMessagesUser
from helpers.helper import get_access_token

fake = Faker()


class TestCreateUser:

    @allure.title("Создание пользователя успешно")
    @allure.description("Успешная регистрация пользователя с валидными данными: проверка возврата токенов и корректных данных пользователя")

    def test_create_user_success(self, cleanup_user):
        payload = {
            "email": f"{fake.user_name()}{fake.random_int()}@test.com",
            "password": fake.password(),
            "name": fake.name()
        }

        response = UserApi.create_user(payload)
        body = response.json()
        user = body["user"]

        token = get_access_token(response)
        cleanup_user.append(token)

        assert response.status_code == 200
        assert body["success"] is True

        assert user["email"] == payload["email"]
        assert user["name"] == payload["name"]

        assert "accessToken" in body
        assert body["accessToken"].startswith("Bearer ")

        assert "refreshToken" in body
        assert isinstance(body["refreshToken"], str)

    


    @allure.title("Нельзя создать пользователя, который уже зарегистрирован")
    @allure.description("Проверка, что система не позволяет создать пользователя с уже существующим email. Ожидается ошибка 403")

    def test_create_duplicate_user(self, cleanup_user):
        payload = {
            "email": f"{fake.user_name()}{fake.random_int()}@test.com",
            "password": fake.password(),
            "name": fake.name()
        }

        response1 = UserApi.create_user(payload)
        assert response1.status_code == 200

        token1 = get_access_token(response1)
        cleanup_user.append(token1)

        response2 = UserApi.create_user(payload)
        body = response2.json()

        with allure.step("Защита от бага: удаление пользователя при неожиданном создании"):
            if response2.status_code == 200:
                token2 = get_access_token(response2)
                cleanup_user.append(token2)

        assert response2.status_code == 403
        assert body["success"] is False
        assert response2.json()["message"] == ResponseMessagesUser.USER_EXISTS_ERROR




    @allure.title("Ошибка при отсутствии почты")
    @allure.description("Проверка, что система не позволяет создать пользователя при отсутствии обязательного поля email, система возвращает ошибку 403")

    def test_create_missing_email(self, cleanup_user):
        payload = {
            "password": fake.password(),
            "name": fake.name()
        }

        response = UserApi.create_user(payload)
        body = response.json()

        with allure.step("Защита от бага: удаление пользователя при неожиданном создании"):
            if response.status_code == 200:
                token = get_access_token(response)
                cleanup_user.append(token)

        assert response.status_code == 403
        assert body["success"] is False
        assert response.json()["message"] == ResponseMessagesUser.NOT_ENOUGH_DATA_ERROR 




    @allure.title("Ошибка при отсутствии пароля")
    @allure.description("Проверка, что система не позволяет создать пользователя при отсутствии обязательного поля password, система возвращает ошибку 403")

    def test_create_missing_password(self, cleanup_user):
        payload = {
            "email": f"{fake.user_name()}{fake.random_int()}@test.com",
            "name": fake.name()
        }

        response = UserApi.create_user(payload)
        body = response.json()

        with allure.step("Защита от бага: удаление пользователя при неожиданном создании"):
            if response.status_code == 200:
                token = get_access_token(response)
                cleanup_user.append(token)

        assert response.status_code == 403
        assert body["success"] is False
        assert response.json()["message"] == ResponseMessagesUser.NOT_ENOUGH_DATA_ERROR 




    @allure.title("Ошибка при отсутствии имени")
    @allure.description("Проверка, что система не позволяет создать пользователя при отсутствии обязательного поля Имя, система возвращает ошибку 403")

    def test_create_missing_name(self, cleanup_user):
        payload = {
            "email": f"{fake.user_name()}{fake.random_int()}@test.com",
            "password": fake.password()
        }

        response = UserApi.create_user(payload)
        body = response.json()

        with allure.step("Защита от бага: удаление пользователя при неожиданном создании"):
            if response.status_code == 200:
                token = get_access_token(response)
                cleanup_user.append(token)


        assert response.status_code == 403
        assert body["success"] is False
        assert response.json()["message"] == ResponseMessagesUser.NOT_ENOUGH_DATA_ERROR 

           

       

        




