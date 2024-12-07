#  Write a program to accept student name and marks from the keyboard and creates a dictionary.
#  Also display student marks by taking student name as input.
num_student = int(input("Enter the number student: "))
student_dict = {}

for item in range(num_student):
    student_name = input("Enter Student name: \n")
    Student_marks = float(int(input("Enter Student marks: \n")))
    student_dict[student_name] = Student_marks

print(student_dict)
