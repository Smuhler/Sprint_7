from conftest import *
from endpoints.courier import *


class TestCreateOrder:

    def test_get_orders_list(self, get_courier):
        courier = Courier(get_courier)
        courier.login()
        response = courier.orders()
        assert response.status_code == 200 and type(response.json()['orders']) == list
