#test_Login.py
import pytest

class TestLogin:
    def test_LoginbyEmail(self,setup):
        print("This is login Email")
        assert True == True

    def test_LoginByFacebook(self,setup):
        print("This is login by Facebook....")
        assert True == True

    def test_LoginByTwitter(self,setup):
        print("This is login by Twitter")
        assert True == True
