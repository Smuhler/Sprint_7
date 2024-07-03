from urls import *
import requests
import json


class Courier:

    def __init__(self, courier):
        self.courier = courier
        self.courier_id = None

    def register(self):
        payload = {
            "login": self.courier[0],
            "password": self.courier[1],
            "firstName": self.courier[2]
        }
        return requests.post(f'{api_v1_url}courier', data=payload)

    def login(self):
        payload = {
            "login": self.courier[0],
            "password": self.courier[1]
        }
        response = requests.post(f'{api_v1_url}courier/login', data=payload)
        if response.status_code == 200:
            self.courier_id = response.json()['id']
        return response

    def delete(self):
        if self.courier_id is None:
            return 'nothing to delete'
        else:
            return requests.delete(f'{api_v1_url}courier/{self.courier_id}')

    def orders(self):
        if self.courier_id is None:
            return 'need login before get orders'
        else:
            return requests.get(f'{api_v1_url}orders?courierId={self.courier_id}')
