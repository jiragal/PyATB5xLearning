import pytest
import allure
import requests


# **********************************************************
# Business has provided below data
# - URL -  https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBooking
# - Method - POST
# - Headers -> Content-Type : application/json
# - Payload - dict
# - Auth  -> NA
# - QP/PP -> NA

class TestClass:
    @allure.title("TC#1 Verify create booking functionality")
    @allure.description("Create Booking CRUD Positive")
    @pytest.mark.crud
    def test_create_booking_positive(self):
        base_url = "https://restful-booker.herokuapp.com"
        base_path_post = "/booking"
        full_url = base_url + base_path_post
        headers = {
            "Content-Type": "application/json"
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

        response_data = requests.post(url=full_url, headers=headers, json=payload)

        # From Here onwards we will check our test_cases
        # Status Code Verification
        assert response_data.status_code == 200;
        # Verify Booking ID > 0, Booking id is not NULL, firstname == "Jim"
        response_data_json = response_data.json()
        bookingid = response_data_json["bookingid"]
        print(bookingid)
        assert bookingid is not None
        assert bookingid > 0
        assert type(bookingid) == int
        # Checking first Name is == 'Jim'
        firstName = response_data_json["booking"]["firstname"]
        assert firstName == 'Jim'
        assert type(firstName) == str

        lastName = response_data_json["booking"]["lastname"]
        totalPrice = response_data_json["booking"]["totalprice"]
        depositPaid = response_data_json["booking"]["depositpaid"]

        assert lastName == 'Brown'
        assert totalPrice == 111
        assert depositPaid == True

        checkIn = response_data_json["booking"]["bookingdates"]["checkin"]
        checkOut = response_data_json["booking"]["bookingdates"]["checkout"]
        assert checkIn == "2018-01-01"
        assert checkOut == "2019-01-01"

        # Check Time response
        time = response_data.elapsed.total_seconds()
        assert time < 5

    # In 2nd test case keeping empty payload and if we check it should hit with 500 error code
    @allure.title("TC#2 Verify that invalid payload is not creating")
    @allure.title("Create Booking CRUD Negative ")
    @pytest.mark.crud
    def test_create_booking_negative_tc1(self):
        base_url1 = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        URL = base_url1 + base_path
        headers = {"Content-Type": "application/json"}
        jason_payload = {}
        response = requests.post(url=URL, headers=headers, json=jason_payload)
        assert response.status_code == 500
        assert response.text == 'Internal Server Error'
