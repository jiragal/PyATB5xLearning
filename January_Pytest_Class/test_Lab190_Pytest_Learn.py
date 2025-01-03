import pytest
import allure
import requests


# pip install pytest allure requests

class TestClass:

    @allure.title("TC#1 Verify that 2+2 == 4")
    @allure.description("This one addition method")
    @pytest.mark.smoketesting
    def test_basic_add(self):
        assert 2 + 2 == 4

    @allure.title("TC#2 Verify that 10 - 5 ==5")
    @allure.description("This is subtract method")
    @pytest.mark.regressiontesting
    def test_basic_subtract(self):
        assert 10 - 5 == 5

    @allure.title("TC#3 Verify that 10*10 ==100")
    @allure.description("This is multiplication method")
    @pytest.mark.smoketesting
    def test_basic_multiplication(self):
        assert 10 * 10 == 100

    #Below method is not ready therefore whenever we run it will skip this method to run
    @pytest.mark.skip(reason="Not working,Skip it")
    def test_sub3():
        assert 0 - 0 != 0

# Below command is used to run particular methods
# pytest -m "smoketesting" January_Pytest_Class/test_Lab190_Pytest_Learn.py

#To generate allure report you can use below two commands and run it, report will generate
#pytest  January_Pytest_Class/test_Lab190_Pytest_Learn.py --alluredir=allure_results1
#allure serve allure_results1