import pytest
import allure
import requests
import pandas as pd
from pandas import isnull

#Returns the ids of all the bookings that exist within the API.
#Can take optional query strings to search and return a subset of booking ids.

url = "https://restful-booker.herokuapp.com"
path_url = "/booking"
class TestClass:
    def test_getbookingIds(self):
        full_url = url + path_url
        response_data = requests.get(url=full_url)
        response_json = response_data.json()
        print(response_json)
        assert response_data.status_code == 200  #Check the status code is 200
        assert response_json is not None         #Check the response body is not empty
        assert type(response_json) == list       #Check the response body is an array
        assert response_data.status_code != 404  #Check the status code is not 404
        assert "specific value" not in response_json #Check the response body does not contain specific value
        assert response_data.status_code != 204      #Check the response body is not null