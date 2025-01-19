# Automation for the Registration Page of the AwesomeQA.com/UI
# Open - https://awesomeqa.com/ui/index.php?route=account/register
# Fill the form
# Verify that next page give - Your Account Has Been Created!
#**************************************************************************#
#Pakge imported
import pytest
import allure
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

#Mainclass Declaration
class TestTask(object):
    @allure.title("Registration Link testing")
    @allure.description("Test to verify user registration is successful")
    @pytest.mark.positive
    def test_account_registration(self):
        load_dotenv()
        # chrome_option = Options()
        # chrome_option.add_argument("--incognito")
        driver = webdriver.Chrome()
        #driver.implicitly_wait(0.5)
        # launch URL
        driver.get(os.getenv("opencart"))
        time.sleep(2)
        f= driver.find_element(By.XPATH,"//input[@id='input-firstname']")
        f.send_keys("name")
        ln=driver.find_element(By.XPATH,"//input[contains(@id,'input-lastname')]")
        ln.send_keys("lastname")
        em=driver.find_element(By.XPATH,"//input[@name='email' and @id='input-email']")
        em.send_keys("admin@opencart.com")
        ph=driver.find_element(By.XPATH,"//input[@name='telephone' and @id='input-telephone']")
        ph.send_keys("919900503274")
        pw=driver.find_element(By.XPATH,"//input[@id='input-password']")
        pw.send_keys("pwd@1234")
        cpw=driver.find_element(By.XPATH,"//input[@id='input-confirm' and @name='confirm']")
        cpw.send_keys("pwd@1234")
        chkbox=driver.find_element(By.XPATH,"//input[@name='agree']")
        chkbox.click()
        button_continue=driver.find_element(By.XPATH,"//*[@id='content'] /form/div/div/input[2]")
        button_continue.click()
        time.sleep(7)
        expected_url ='https://awesomeqa.com/ui/index.php?route=account/success'
        assert driver.current_url == expected_url
        print(driver.title)
        driver.close()




