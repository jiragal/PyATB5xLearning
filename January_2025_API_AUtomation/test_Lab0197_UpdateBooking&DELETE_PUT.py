import pytest
import allure
import requests

# Booking - UpdateBooking***********************************************************#
# Here first to update id we need to get "token" and then we need "bookingid" ******#
# We have defined 3 different methods "get_booking_id()" & get_token()              #
# In third method we are updating id field                                          #
# Booking - UpdateBooking***********************************************************#
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}


def get_token():
    base_path = "/auth"
    full_url = base_url + base_path

    # 3rd Part is "Payload" that is Request body
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    base_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
    base_json_response = base_data.json()
    assert base_data.status_code == 200
    token = base_json_response["token"]
    print(token)
    assert type(token) == str
    assert len(token) > 0
    return token

def get_booking_id():
    base_path = "/booking"
    full_url = base_url+ base_path
    json_payload = {
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
    response_body = requests.post(url=full_url,headers=headers,json=json_payload)
    response_body_json = response_body.json()
    booking_id = response_body_json["bookingid"]
    return booking_id

def test_put_request():
    token = get_token()
    bookingid = get_booking_id()
    print(token)
    print(bookingid)
    base_path = "/booking/" + str(bookingid)
    full_url_put = base_url + base_path
    cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }
    json_payload = {
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=full_url_put, headers=headers, json=json_payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Pramod"

def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = get_booking_id()
    DELETE_URL = URL + str(booking_id)
    cookie_value ="token=" + get_token()
    headers = {
        "Cookie": cookie_value,
        "Content-Type": 'application/json'
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201
