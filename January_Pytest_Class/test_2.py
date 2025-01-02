import pytest
#Our Requirement is before running every test methods:
#We should run normal method


class TestClass:

    @pytest.fixture()    #Decorator
    def setup(self):
        print("Launching Browser")    #Execute before every method
        print("Open Application")
        yield
        print("Closing Browser ...")  #Execute after every method

    def test_Login(self,setup):
        print("This is Login Test")

    def test_Search(self,setup):
        print("This is search test")

    def test_AdvanceSearch(self,setup):
        print("This is advance search test")

