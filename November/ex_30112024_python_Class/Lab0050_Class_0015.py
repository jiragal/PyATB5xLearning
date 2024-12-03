# Usually when we are creating object it will takes space inside
# Therefore in General programmer will sometime delete thos space

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Shradha")
print(s1.name)
del s1     # Here deleting the object
print(s1.name)
