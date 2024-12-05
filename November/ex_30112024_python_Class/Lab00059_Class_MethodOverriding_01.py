# Over-ridden concept
class Parent:
    def home(self):
        print("2BHK")


class Son(Parent):
    def home(self):
        print("3BHK")

    def town(self):
        print("10BHK")


obj_Ref = Son()
obj_Ref.home()
obj_Ref.town()
