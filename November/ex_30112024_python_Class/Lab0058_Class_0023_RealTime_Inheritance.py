# Here Pramod covered real time example for Inheritabce:
#In the below example class "Base Test" is common for both the TestCase1 and TestCase2 class
class BaseTest:
    def open_browser(self):
        print("Starting the Browser")

    def close_browser(self):
        print("Close Browser")


class TestCase1(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("Positive Test Case1 is executed")
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Negative Test Case2 is executed")
        self.close_browser()

class TestCase2(BaseTest):
    def test_2_postive(self):
        self.open_browser()
        print("Postove Test Case2 Executed")
        self.close_browser()

    def test_2_negative(self):
        self.open_browser()
        print("Negative Test Case2 is executed")
        self.close_browser()







