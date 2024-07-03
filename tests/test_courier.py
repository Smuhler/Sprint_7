from conftest import *
from endpoints.courier import *
from unittest.mock import patch
from urls import *
import requests


class TestCourierRequest:

    @allure.title('Проверка Регистрации')
    @allure.description('Генерируем данные и регистрируемся')
    def test_register_is_correct(self, get_courier_data):
        courier = Courier(get_courier_data)
        response = courier.register()
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Проверка Регистрации одинаковых пользователей')
    @allure.description('Генерируем данные, регистрируемся дважды с одинаковыми данными')
    def test_register_duplicates_failed(self, get_courier):
        courier = Courier(get_courier)
        response = courier.register()
        assert response.status_code == 409 and response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Проверка авторизации после регистрации')
    @allure.description('Генерируем данные, регистрируемся и авторизуемся')
    def test_register_and_login_is_correct(self, get_courier):
        courier = Courier(get_courier)
        response = courier.login()
        assert response.status_code == 200 and response.json() == {'id': response.json()['id']}

    @allure.title('Проверка регистрации без логина')
    @allure.description('Генерируем данные и пытаемся зарегистрироваться')
    def test_register_without_login_failed(self, get_courier_data):
        courier = Courier(['', get_courier_data[1], get_courier_data[2]])
        response = courier.register()
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Проверка регистрации без пароля')
    @allure.description('Генерируем данные и пытаемся зарегистрироваться')
    def test_register_without_password_failed(self, get_courier_data):
        courier = Courier([get_courier_data[0], '', get_courier_data[2]])
        response = courier.register()
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
