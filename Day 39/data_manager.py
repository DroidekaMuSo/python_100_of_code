import os
import requests
from requests.auth import HTTPBasicAuth

SHEETY_ENDPOINT = "https://api.sheety.co/9522b4bb4df77f7c1b20684a3bffc823/flightDeals/prices"


class DataManager:
    def __init__(self):
        self._user = "....."
        self._password = "....."
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.hearders = {
            "Authorization": "Basic ....."
        }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.hearders)
        response.raise_for_status()
        data = response.json()

        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.hearders
            )
            print(response.text)
