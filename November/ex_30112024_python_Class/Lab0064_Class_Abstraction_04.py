from abc import ABC, abstractmethod


class ExcelReader(ABC):  # If we need to see the effect of Abstraction Class we need use "ABC

    def readFromExcel(self):
        pass


class Browser(ExcelReader):
    def start_Browser(self):
        pass

    def stopBrowser(self):
        pass


class TC1(Browser):
    def start_Browser(self):
        print("Start Browsing")

    def stopBrowser(self):
        print("Stop Browsing")

    def readFromExcel(self):
        print("Excel is ready for reading")

    def runTC(self):
        self.start_Browser()
        self.readFromExcel()
        self.stopBrowser()


# Object Creating
tc1 = TC1()
tc1.runTC()

#Abstraction Real meaning is: Force something to child
