import pytest
import allure
import requests

from January_Pytest_Class.PostRequest_API_Automation.test_Lab192_Pytest_POST_Token import headers


class Test_Class:
    def test_createToken(self):
        #1st part is URL
        url = "https://restful-booker.herokuapp.com/"
        path_url ="/auth"
        full_url=url+path_url

        #2nd Part is Header
        header= {"Content-Type": "application/json"}

        #3rd Part is "Payload" that is Request body
        json_payload_auth = {
            "username":"admin",
            "password":"password123"
        }

        #Here we are using POST method
        response_data=requests.post(url=full_url,headers=header,json=json_payload_auth)
        print(response_data)
        assert response_data.status_code == 200
        get_response_json = response_data.json()
        #ResponseBody
        token = get_response_json["token"]
        print(token,len(token))
        assert type(token) == str
        assert len(token) > 0
        # header_response = response_data.headers
        # print(header_response)
        #Check Response body does not contain error message
        assert 'error' not in get_response_json
        elapsed_time = response_data.elapsed.total_seconds()
        assert elapsed_time <= 2000
        print(elapsed_time)







