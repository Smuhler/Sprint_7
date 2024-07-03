from conftest import *
from data import colours
from endpoints.orders import *
from endpoints.courier import *
from unittest.mock import patch
from urls import *
import requests


class TestCreateOrder:

    @pytest.mark.parametrize('colour', colours)
    def test_create_order(self, colour):
        response = Order.create_order(colour)
        assert response.json() == {'track': response.json()['track']}
