# Class and Object in Python
#A class is Blueprint
#A class is collection of variables(attributes) and methods(Behaviour)
#A class is a logical entity
#It does not occupy space in the memory
class Student:
    name = "Karun kumar"


# creating object
#An object is instance of class
#An object is physical entity
#As soon as once create object, it will acquire all the properties from class.
#For one class we can create multiple objects.
#Objets are independent.
s1 = Student()  # instance of object here object is "s1"
print(s1.name)

# Creating One more Object
# Here we can observe every time same name is printing
s2 = Student()
print(s2.name)

#Functions vs Method
#Function ----> We are creating without class
#Method ------> Created inside the class

