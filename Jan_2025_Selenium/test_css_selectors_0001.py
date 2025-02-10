#CSS SLECTORS
#1) tag id
#2) tag class
#3) tag attribute    Syntax---> tagname[attribute=value]
#4) tag, class and attributes
#tag is optional
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_css_selector():
    driver=webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    #1) tag id
    #find elements  tagname#ValueofId  tagname is optional
    #driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("sjiraga@gmail.com")
    # driver.find_element(By.CSS_SELECTOR,"#email")

    #2)tag class   Syntax---> tagname.ValueOfClass
    # driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc2gmail.com")


    #3) tag attribute  We can use any attribute Syntax---> tagname[attribute=value]
    # driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal-email']").send_keys("abc.gmail.com")


    #4)tag, class & attribute
    driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("abc")
    time.sleep(5)



