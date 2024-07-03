from urls import *
import requests
import allure


class Courier:

    def __init__(self, courier):
        self.courier = courier
        self.courier_id = None

    @allure.step('Регистрируемся')
    def register(self):
        payload = {
            "login": self.courier[0],
            "password": self.courier[1],
            "firstName": self.courier[2]
        }
        return requests.post(courier_url, data=payload)

    @allure.step('Авторизуемся')
    def login(self):
        payload = {
            "login": self.courier[0],
            "password": self.courier[1]
        }
        response = requests.post(login_url, data=payload)
        if response.status_code == 200:
            self.courier_id = response.json()['id']
        return response

    @allure.step('Удаляем пользователя')
    def delete(self):
        if self.courier_id is None:
            return 'nothing to delete'
        else:
            return requests.delete(f'{delete_url}{self.courier_id}')

    @allure.step('Получаем список заказов')
    def orders(self):
        if self.courier_id is None:
            return 'need login before get orders'
        else:
            return requests.get(f'{orders_by_id_url}{self.courier_id}')
