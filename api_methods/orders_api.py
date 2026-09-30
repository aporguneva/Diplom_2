import requests
from urls import Url
import allure

class OrdersApi:
    @staticmethod
    @allure.step("Запрс на Создание заказа")
    def create_order(order_data, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token

        return requests.post(
            f"{Url.BASE_URL}{Url.CREATE_ORDER}", 
            json=order_data, 
            headers=headers)