# that's correct. In Python, any parameters that come after a single asterisk (*)
# in a function definition must be called using keyword arguments.
def example_function(a,b,*,c,d):
    print(a,b,c,d)

#This is valid
example_function(1,2,c=3,d=4)

#This is not valid
    # example_function(1,2,3,4)
    # We will get "TypeError: example_function() takes 2 positional arguments but 4 were given"

name = "Pramod"
print(f"hello {name[::-1]}")

def greet(*,name,reverse=False,debug=False):
    if debug:
        print("You called greet function")
    if reverse:
        print(f"Hello your name will be reversed{name[::-1]}")
    return f"hello {name}"

greet(name="Pramod",reverse=True,debug=False)
#Below function is used to add number and using *args--It means We can pass n-number of values or nothing
def add_numbers(*args):
    total =0.00
    for item in args:
        total = total + item
    return total

print(add_numbers())                   #Passing nothing
print(add_numbers(10))                 #Passing only one value
print(add_numbers(10,100,1000))  #Passing 3 item and adding all of them
nums = [1,2,3,4]
print(type(nums))
print(type(add_numbers(*nums)))