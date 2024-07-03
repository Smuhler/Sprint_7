import pytest
from helpers import *
from endpoints.courier import *


@pytest.fixture(scope="function")
def get_courier():
    courier = register_new_courier_and_return_login_password()
    yield courier
    if len(courier) == 3:
        courier_to_delete = Courier(courier)
        courier_to_delete.login()
        courier_to_delete.delete()


@pytest.fixture(scope="function")
def get_courier_data():
    courier_data = create_data_for_courier_register()
    yield courier_data
    courier_to_delete = Courier(courier_data)
    if courier_to_delete.login().status_code == 200:
        courier_to_delete.delete()
