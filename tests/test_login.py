import allure
from api_methods.user_api import UserApi
from data.data import ResponseMessagesUser

class TestLogin:
    @allure.title("Проверка успешной авторизации")
    @allure.description("Проверка, что при успешном входе в систему возвращается корректный ответ с токенами и данными пользователя")
    def test_login_user_success(self, new_user):
        payload = new_user["payload"]
        email = payload["email"]
        password = payload["password"]
        
        response = UserApi.login_user(email, password)

        body = response.json()
        user = body["user"]

        assert response.status_code == 200
        assert body["success"] is True

        assert user["email"] == payload["email"]
        assert user["name"] == payload["name"]

        assert "accessToken" in body
        assert body["accessToken"].startswith("Bearer ")

        assert "refreshToken" in body
        assert isinstance(body["refreshToken"], str)



    @allure.title("Авторизация с неверным паролем")
    @allure.description("Проверка, что при попытке авторизации с неправильным паролем возвращается ошибка 401 с сообщением 'email or password are incorrect'")
    def test_login_wrong_password(self, new_user):
        payload = new_user["payload"]
        email = payload["email"]

    
        response = UserApi.login_user(email, "wrong_password")

        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert response.json()["message"] == ResponseMessagesUser.LOGIN_ERROR
    


    @allure.title("Авторизация с неверным email")
    @allure.description("Проверка, что при попытке авторизации с неправильным email возвращается ошибка 401 с сообщением 'email or password are incorrect'")
    def test_login_wrong_login(self, new_user):
        payload = new_user["payload"]
        email = payload["email"]
        password = payload["password"]

    
        response = UserApi.login_user("wrong_email", password)
        
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert response.json()["message"] == ResponseMessagesUser.LOGIN_ERROR


    @allure.title("Авторизация без пароля")
    @allure.description("Проверка, что при попытке авторизации без пароля возвращается ошибка 401 с сообщением 'email or password are incorrect'")
    def test_login_missing_password(self, new_user):
        payload = new_user["payload"]
        email = payload["email"]
        
        response = UserApi.login_user(email, "")

        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert response.json()["message"] == ResponseMessagesUser.LOGIN_ERROR


    @allure.title("Авторизация без email")
    @allure.description("Проверка, что при попытке авторизации без email возвращается ошибка 401 с сообщением 'email or password are incorrect'")
    def test_login_missing_email(self, new_user):   
        payload = new_user["payload"]
        password = payload["password"]
        
        response = UserApi.login_user("", password)

        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert response.json()["message"] == ResponseMessagesUser.LOGIN_ERROR



    @allure.title("Авторизация несуществующего пользователя")
    @allure.description("Проверка, что при попытке авторизации с данными несуществующего пользователя возвращается ошибка 401 с сообщением 'Учетная запись не найдена'")
    def test_login_nonexistent_user(self):
        response = UserApi.login_user("fake_login_123", "fake_password_123")

        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert response.json()["message"] == ResponseMessagesUser.LOGIN_ERROR

    




       

        



