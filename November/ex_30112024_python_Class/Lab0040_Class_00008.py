#Static Method Method dont use the self paramter

class Student:
    @staticmethod
    def college():
        print("ABC College")

#Decorators allow us to wrap another function in order to extend the behaviour
#of the wrapped function. without permently modifying it
 #@staticmethod: It will transform method into a static method
 #A static method is form of decorator function.
 #A static method either called class C.f() or an instance C().F()
 #