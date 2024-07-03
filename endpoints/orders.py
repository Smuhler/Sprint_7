from urls import *
import requests
import json


class Order:

    @staticmethod
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
        return requests.post(f'https://qa-scooter.praktikum-services.ru/api/v1/orders', data=json.dumps(payload))


