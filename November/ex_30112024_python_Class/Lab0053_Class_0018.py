# Inheritance:
# When one class derives the properties and methods of another class
# We will inherit the characters from our parents.
# Inheritance is a fundamental concept in object oriented programming language
# It allows new class to based on existing or old class property or attribute can inherit
# A child class can inherit parents attribute and Behaviours
# Types of Inheritance:
#       1) Single Inheritance ---A child clss inherits from a single parent class
#       2) Multiple Inheritance ---A child class can inherits from two or more parent classes
#      3) Multileval Inheritance: A child can inherit from ---Grand-parent, Parents...like Father and Father
#     4)Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
#     5)Hybrid Inheritance: Combination of two or more types of inheriting

# Single Inheritance
class Father:
    key = "2BHK"

    def car(self):
        print("Father has a car -> Alto")
        print(self.key)


# 2nd class
class Son(Father):  #Single Inheritance
    key2 = "3BHK"

    def suvcar(self):
        print("MG Hector Red")
        print(self.key2)


# Object Creator
obj1 = Father()
print(obj1.key)
print(obj1.car())

#Son Object
obj2 = Son()
print(obj2.key2)
print(obj2.key)
print(obj2.car())
