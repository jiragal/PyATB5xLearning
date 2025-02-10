from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()

#XPATH AXES  ---->   self
txt_msg= driver.find_element(By.XPATH,"//a[contains(text(),'HFCL')]/self::a").text
time.sleep(5)
print(txt_msg)

#XPATH AXES -----> Parent
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'HFCL')]/parent::td").text
print(text_msg)

#XPATH AXES ------>Child ---To access child first we moved towards "ancestor"
# and then we find out all the child's
child = driver.find_elements(By.XPATH,"//a[contains(text(),'HFCL')]/ancestor::tr/child::td")
print(len(child))
for item in child:
    print(f"{item.text}")

#XPATH AXES ---Ancestor
ancestor = driver.find_element(By.XPATH,"//a[contains(text(),'HFCL')]/ancestor::tr").text
print(ancestor)   #HFCL A 98.00 106.07 + 8.23 Buy  |  Sell

#XPATH AXES ---Ancestor

driver.quit()