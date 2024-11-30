#  __init__ function
# Constructor --All class have function called __init__ function
#                   which is always executed when the object is being initiated.

# Here We have tried to show how constructor is creating and how it works
# How self parameter works
# With the Help of "self" parameters we are creating different variables(where data can be stored)
class Student:

    # Constructor Creating
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks


# Variables and attributes both are same in the above example it is called as "fullname"

s1 = Student("Pramod", 100)  # Object creating
print(s1.name, s1.marks)

# 2nd Object
s2 = Student("Sanjiva", 101)
print(s2.name, s2.marks)
