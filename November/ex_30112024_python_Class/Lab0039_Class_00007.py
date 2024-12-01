# Create a Student class that takes "name", "marks" of 3 subject as arguments in constructor
# Then create method to pring an average

class Student:
    @staticmethod
    def college():
        print("ABC College")
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def get_ave_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average marks is: ", sum / 3)


l1 = [99, 98, 90]
s1 = Student("Tony waugh", l1)
s1.get_ave_marks()
s1.college()
