# Class and Instance Attributes
# 1.Class attributes       ----For full class same i.e for all the objects it is same
# 2.Instance attributes    ----For each objects attribute change

class Student:
    college_name = 'New Horizon'
    def __init__(self, name, grade, sect):
        self.name = name
        self.grade = grade
        self.sect = sect
        print("This is information of Student")


s3 = Student("Pramod", 10, "10B")
print(s3.college_name)
print(s3.name, s3.grade, s3.sect)

s1 = Student("Karan",5,'5A')
print(s1.college_name)
print(s1.name)
print(s1.grade)
print(s1.sect)
