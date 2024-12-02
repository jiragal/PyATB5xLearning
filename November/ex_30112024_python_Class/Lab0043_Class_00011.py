# Web automation selenium
# Page you are going to automate
class VWOLoginPage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "jiragal@gmail.com" and self.password == "Pass1234":
            print("Allowed, Login Successful ")
        else:
            print("Login Failed")


email = input("Enter your email-id \n")
password = input("Enter your password: \n")

vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()