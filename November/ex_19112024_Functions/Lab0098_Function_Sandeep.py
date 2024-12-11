# Function Annotations
# Annotations are only type hints. But it does not enforce type check!



def add(a: int, b: int):
    return a+b

print(add(2.00,2))
#***************************************************************************************#
my_age = 10

def myinfo(myname,age=my_age):
    print(myname,age)

print(myinfo('pradeep',50))    # Prints(pradeep, 50)
print(myinfo('steve'))                      # Prints(steve, 10)
age = 20
print(myinfo('rubi'))                       #prints(rubi,10)
#***************************************************************************************#
# names=[] in the function declaration makes Python essentially do this:
""" 
1. This function has a parameter named "names" its default argument is []
let's set this particular [] aside and use it anytime there's no para
2. Every time the function is called, create a variable "names",  
& the passed parameter or the value we set aside earlier
"""
def func(namey = []):
    namey.append(1)
    return namey

a = func()
func()
print(a)
func()
print(a)
print(func([10, 20, 30, 40]))
