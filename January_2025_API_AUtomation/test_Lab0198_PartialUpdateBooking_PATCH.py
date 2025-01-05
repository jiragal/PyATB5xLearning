import pytest
import allure
import requests

from January_Pytest_Class.PostRequest_API_Automation.test_Lab192_Pytest_POST_Token import headers

@allure.description("TC#1 Verify get token is successful or not")
@pytest.mark.smoketesting
def get_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"
    full_url = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    base_requests = requests.post(url=full_url, headers=headers, json=payload)
    base_json_response = base_requests.json()
    assert base_requests.status_code == 200
    token = base_json_response["token"]
    return token


def get_booking_ids():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    base_requests1 = requests.post(url=full_url, headers=headers, json=payload)
    base_response_jsons = base_requests1.json()
    booking_id = base_response_jsons["bookingid"]
    return booking_id


def test_patch_requests():
    token = get_token()
    bookingids = get_booking_ids()
    base_urls = "https://restful-booker.herokuapp.com"
    base_paths = "/booking/" + str(bookingids)
    full_url = base_urls + base_paths
    cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Cookie":cookie
    }
    payloads = {
        "firstname": "James",
        "lastname": "Anaveer"
    }
    base_request = requests.patch(url=full_url,headers=headers,json=payloads)
    json_responses = base_request.json()
    assert base_request.status_code == 200
    assert json_responses["firstname"] == "James"
    assert json_responses["lastname"] == "Anaveer"
