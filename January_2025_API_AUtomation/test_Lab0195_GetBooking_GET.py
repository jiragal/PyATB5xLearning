import pytest
import allure
import requests


class TestClass:
    def test_getBooking(self):
        url = "https://restful-booker.herokuapp.com/booking"
        path_url = "/1"
        full_url = url + path_url
        header = {"Accept": "application/json"}
        response_data = requests.get(url=full_url, headers=header)
        response_json = response_data.json()
        assert response_data.status_code == 200
        assert response_json is not None
        print(response_json)
        # Check Time response
        time =  response_data.elapsed.total_seconds()
        assert time < 500
        print(response_json)
        assert "firstname" in response_json
        #This logic will tell you how to check all the keys are present or not?
        required_keys = ["firstname","lastname","totalprice","depositpaid","bookingdates"]
        assert all(key in response_json for key in required_keys),"Missing keys: " + str(set(required_keys) - set(response_json))
        #Check first Name is present in response or not
        assert response_json['firstname'] == 'Sally'

