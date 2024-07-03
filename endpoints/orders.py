from urls import *
import requests
import json
import allure


class Order:

    @staticmethod
    @allure.step('Создаем заказ')
    def create_order(colour):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colour
        }
        return requests.post(create_order_url, data=json.dumps(payload))


