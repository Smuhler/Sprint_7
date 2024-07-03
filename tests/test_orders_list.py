from conftest import *
from endpoints.courier import *


class TestCreateOrder:

    @allure.title('Проверка получения списка заказов пользователя')
    @allure.description('Создаем пользователя, авторизуемся и проверяем, что возвращается список заказов')
    def test_get_orders_list(self, get_courier):
        courier = Courier(get_courier)
        courier.login()
        response = courier.orders()
        assert response.status_code == 200 and type(response.json()['orders']) == list
