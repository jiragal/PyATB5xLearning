import pytest
import allure
import requests


# Creates a new booking in the API by POST method
class TestClass:
    @allure.title("TC#1 Verify create booking functionality")
    @allure.description("Positive functionality testing")
    @pytest.mark.crud_positive_test_case
    def test_createbooking(self):
        url = "https://restful-booker.herokuapp.com"
        path_url = "/booking"
        full_url = url + path_url
        headers = {
            "Content-Type":"application/json",
            "Accept":"application/json"
        }
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response_body = requests.post(url=full_url,headers=headers,json=payload)
        response_json = response_body.json()
        print(response_json)
        booking_id = response_json["bookingid"]
        print(booking_id)
        # TC#1 Verify that first name should be equal to Jim"
        first_name = response_json["booking"]["firstname"]
        assert first_name == 'Jim'
        #TC#2  Verify that status code eq to 200 OK
        assert response_body.status_code == 200
        #TC#3 Verify the execution time below 500ms
        time = response_body.elapsed.total_seconds()
        assert time <= 500
        #TC#4 Test to verify header verification
        response_header = response_body.headers["Content-Type"]
        header_response = response_header[:16]
        assert header_response == "application/json"
        #TC#5 Verify that booking Key is present in response
        empty_list = []
        for key, value in response_json.items():
            if key not in empty_list:
                empty_list.append(key)
            else:
                continue
        assert "bookingid" in empty_list
        # TC#5 ENDS
        #Negative Test Cases
    @allure.title("TC#2 Verify that invalid payload is not creating")
    @allure.description("If payload is empty then response code is 500")
    @pytest.mark.crud.negative
    def test_create_booking_negative(self):
        url1 = "https://restful-booker.herokuapp.com"
        path_url1 = "/booking"
        full_url1 = url1 + path_url1
        headers1 = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        jason_payload1 = {}
        client_response = requests.post(url=url1,headers=headers1,json=jason_payload1)
        response_json1 = client_response.json()
        assert client_response.status_code == 200