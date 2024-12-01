# Methods:   Methods are basically functions that belong to object
# We are defining these methods inside class
# Still now we have learned "String method, List method and Dictionary method"
# For allthese already inbuilt class were there we just referred

# Example:
class Student:
    college_name = "ABC college"

    def __init__(self, fullname, grade):
        self.name = fullname
        self.grade = grade

    def wellcome(self):
        print("Wellcome to our College",s1.name)

    def names(self):
        print(s1.name)


s1 = Student("pawan", "First_Class")
print(s1.name, "is ",s1.grade, "Student")
s1.wellcome()
s1.names()


