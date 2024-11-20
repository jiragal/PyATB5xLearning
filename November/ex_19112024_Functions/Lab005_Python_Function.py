# Python functions are reusable blocks of code that performs a specific task.
# Python functions are defined using the def keyword.

#############################################################################################
# Here’s an example of a simple function definition which purpose is to print Hello each time it’s called
def greet():
    print('Hello how are you!')

greet()

#############################################################################################
# Here in this example passing single argument anf displays each time when it is called
def greet_two(greet):
    print(greet)

greet_two("Howdy, Sanjiva")
greet_two("Howdy, Pramod")
#############################################################################################

# In the 3rd example passing default value, if no arguments passed
def greet_3(greeting='Hello'):
    print(greeting)


greet_3()
greet_3('Hi')
greet_3('Dude')
#############################################################################################
# A function that reaches the end of execution without a return statement will always return None:
def do_nothing():
    pass
print(do_nothing())
#############################################################################################
#                           Function with return values         ############
def add_two_numbers(num1, num2):
    return num1 + num2

add1 = add_two_numbers(2,99)
print('add1 values is:', add1)
#############################################################################################