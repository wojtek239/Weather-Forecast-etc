import requests


class ConnectionMixin:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def connect_to_api(self, params):
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error connecting to API:", response.text)
            return None
