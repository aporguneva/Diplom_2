import allure
from api_methods.user_api import UserApi
from api_methods.orders_api import OrdersApi
from data.data import ResponseMessagesOrder
from data.order_data import OrderData


class TestCreateOrder:


    @allure.title("Создание заказа с авторизацией и с ингредиентами")
    @allure.description("Проверка, что авторизованный пользователь может создать заказ с валидными ингредиентами")

    def test_create_order_success_with_login(self, login_user):
        
        access_token = login_user["access_token"]

        response = OrdersApi.create_order(OrderData.valid_ingredients, access_token)

        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True

        assert "name" in body
        assert "бургер" in body["name"]
        
        assert "order" in body
        assert "number" in body["order"]
        assert isinstance(body["order"]["number"], int)


    @allure.title("Создание заказа без авторизации и с ингредиентами")
    @allure.description("Проверка, что НЕ авторизованный пользователь может создать заказ с валидными ингредиентами")

    def test_create_order_success_without_login(self):

        response = OrdersApi.create_order(OrderData.valid_ingredients)

        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True

        assert "name" in body
        assert "бургер" in body["name"]

        assert "order" in body
        assert "number" in body["order"]
        assert isinstance(body["order"]["number"], int)


    @allure.title("Создание заказа с авторизацией, но без ингредиентами")
    @allure.description("Проверка, что авторизованный пользователь НЕ может создать заказ без ингредиентов, возвращается код ошибки 400")

    def test_create_order_without_ingr_with_login(self, login_user):
        
        access_token = login_user["access_token"]

        response = OrdersApi.create_order(OrderData.empty_ingredients, access_token)

        body = response.json()

        assert response.status_code == 400
        assert body["success"] is False
        assert body["message"] == ResponseMessagesOrder.EMPTY_CART_ERROR

    
    @allure.title("Создание заказа без авторизации и без ингредиентов")
    @allure.description("Проверка, что НЕ авторизованный пользователь НЕ может создать заказ без ингредиентов, возвращается код ошибки 400")

    def test_create_order_without_ingr_without_login(self):

        response = OrdersApi.create_order(OrderData.empty_ingredients)

        body = response.json()

        assert response.status_code == 400
        assert body["success"] is False
        assert body["message"] == ResponseMessagesOrder.EMPTY_CART_ERROR



    @allure.title("Создание заказа без авторизации и невалидным хэшом ингрелиентов")
    @allure.description("Проверка, что НЕ авторизованный пользователь НЕ может создать заказ c невалидным хэшом ингредиентов, возвращается код ошибки 500")

    def test_create_order_with_invalid_hash_without_login(self):

        response = OrdersApi.create_order(OrderData.invalid_hash_ingredients)


        assert response.status_code == 500
        assert "Internal Server Error" in response.text
        


    @allure.title("Создание заказа с авторизацией, и невалидным хэшом ингрелиентов")
    @allure.description("Проверка, что авторизованный пользователь НЕ может создать заказ c невалидным хэшом ингредиентов, возвращается код ошибки 500")

    def test_create_order_with_invalid_hash_with_login(self, login_user):
        
        access_token = login_user["access_token"]

        response = OrdersApi.create_order(OrderData.invalid_hash_ingredients, access_token)


        assert response.status_code == 500
        assert "Internal Server Error" in response.text
        

        