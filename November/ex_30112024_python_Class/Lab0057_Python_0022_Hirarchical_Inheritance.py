# Hirarchical Inheritance
class Father:
    def bhk1(self):
        print("1BHK-Father House")


class Pramod(Father):
    def bhk2(self):
        print("2BHK Prmod Property")


class Amit(Father):
    def bhk3(self):
        print("3BHK Amit Property")


class Lucky(Father):
    def bhk0(self):
        print("NO HOUSE")


obj1 = Pramod()
print(obj1.bhk1())
print(obj1.bhk2())
#Pramod cannot access others but only Fathers like this Hirarchial Works