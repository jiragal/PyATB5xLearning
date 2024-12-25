# There are two types of methods inside Class.
# Instance method  ---> We can call only through object
# Static method ------> We can directly call using Class
# When we create @staticmethod that is common for every object.
# annotation  @staticmethod

class Myclass:
    def m1(self):
        print("This is instance method")

    @staticmethod
    def m2(self, num):
        print(self)
        print(num)

#By Instance method
mc1 = Myclass()
mc1.m1()
mc1.m2(100,200)

#By static method
Myclass.m2(10,20)


