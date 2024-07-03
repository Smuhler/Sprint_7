from conftest import *
from data import colours
from endpoints.orders import *


class TestCreateOrder:

    @allure.title('Проверка функционала создания заказа с выбором цвета')
    @allure.description('Создаем заказ с набором цветов {colour}')
    @pytest.mark.parametrize('colour', colours)
    def test_create_order(self, colour):
        response = Order.create_order(colour)
        assert response.json() == {'track': response.json()['track']}
