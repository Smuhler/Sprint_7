from conftest import *
from endpoints.courier import *
from unittest.mock import patch
from urls import *
import requests


class TestLoginRequest:

    @allure.title('Проверка авторизации')
    @allure.description('Генерируем данные, регистрируемся и авторизуемся')
    def test_login_is_correct(self, get_courier):
        courier = Courier(get_courier)
        response = courier.login()
        assert response.status_code == 200 and response.json() == {'id': response.json()['id']}

    @allure.title('Проверка авторизации без логина')
    @allure.description('Регистрируемся и пытаемся войти без логина')
    def test_login_without_login(self, get_courier):
        courier = Courier(['', get_courier[1], get_courier[2]])
        response = courier.login()
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Проверка авторизации без пароля')
    @allure.description('Регистрируемся и пытаемся войти без пароля')
    def test_login_without_password(self, get_courier):
        courier = Courier([get_courier[0], '', get_courier[2]])
        response = courier.login()
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Проверка авторизации с неправильным логином')
    @allure.description('Регистрируемся и пытаемся войти с неправильным логином')
    def test_login_incorrect_login(self, get_courier):
        courier = Courier(['incorrectLogin', get_courier[1], get_courier[2]])
        response = courier.login()
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Проверка авторизации с неправильным паролем')
    @allure.description('Регистрируемся и пытаемся войти с неправильным паролем')
    def test_login_incorrect_password(self, get_courier):
        courier = Courier([get_courier[0], 'incorrectPassword', get_courier[2]])
        response = courier.login()
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
