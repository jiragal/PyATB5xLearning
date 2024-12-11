from Python_Module_concept.Lab0107_OpenBrowser import openBrowser
from Python_Module_concept.Lab0108_CloseBrowser import stopBrowser

openBrowser()
print("Browser is running")
stopBrowser()

#Same above thing we are achiving through function
def test_case(name):
    openBrowser()
    print(f"Hello {name} Browser is running ")
    stopBrowser()

test_case('pradeep')

#Same above thing we can achieve through Class Function
class TestClass:
    def unit_test(self,name):
        self.name = name
        openBrowser()
        print(f"Hello {name} browser is running")
        stopBrowser()

obj_unit_test = TestClass()
obj_unit_test.unit_test('ruby')


















