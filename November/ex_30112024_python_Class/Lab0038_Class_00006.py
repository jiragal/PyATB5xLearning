# Methods:   Methods are basically functions that belong to object
# We are defining these methods inside class
# Still now we have learned "String method, List method and Dictionary method"
# For all these already inbuilt class were there we just referred

# Example:
class Student:
    college_name = "ABC college"

    def __init__(self, fullname, grade):
        self.name = fullname
        self.grade = grade

    def wellcome(self):
        print("Wellcome to our College", s1.name)

    def names(self):
        print(s1.name)


s1 = Student("pawan", "First_Class")
print(s1.name, "is ", s1.grade, "Student")
s1.wellcome()
s1.names()


# method VS constructor
# For method can give any name
# return any value
# method can take arguments/parameters

# Constructor name should be always __init__(self)
# The constructor will not return any value
# The constructor can also take arguments and parameters
# The constructor will be called at the time of object creation

class Miclass:
    def __int__(self):
        print("This is constructor")

    def m1(self):
        print("This is normal method")

