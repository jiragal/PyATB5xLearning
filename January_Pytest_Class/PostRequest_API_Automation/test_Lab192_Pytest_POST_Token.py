# Creates a new auth token to use for access to the PUT and DELETE /booking
# ***********************************************************************************#
# Business has provided below data
# - URL -  https://restful-booker.herokuapp.com/auth
# - Method - POST
# - Headers -> Content-Type : application/json
# - Payload - dict
# - Auth  -> yes
# - QP/PP -> NA
# ***********************************************************************************#
import pytest
import allure
import requests

# pip install pytest allure requests
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}


class TestClass:
    def test_create_token(self):
        path_url = "/auth"
        full_url = base_url + path_url
        json_payload_auth = {
            "username": "admin",
            "password": "password123"
        }
        response_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
        print(response_data)
        assert response_data.status_code == 200
        response_data_json = response_data.json()
        token = response_data_json["token"]
        print(token)
        assert type(token) == str
        assert len(token) > 0
