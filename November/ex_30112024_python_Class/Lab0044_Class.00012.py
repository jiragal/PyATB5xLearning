# Web Automation -Selenium
# Page - You are going to automate
from dotenv import load_dotenv
import os


class GmailLoginPage:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirmation(self):
        if self.email == "jiragal@gmail.com" and self.password == "Pass1234":
            print("Allowed Loging Page")
        else:
            print("Login Failed")


load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(email, password)

vmo_login = GmailLoginPage(email,password)
print(vmo_login.login_confirmation())

