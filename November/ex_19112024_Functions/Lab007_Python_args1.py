# Usage of **args--This means passing numbers of arguments i. unlimited numbers of arguments you can pass
def print_mul_arg(*args):
    for i in args:
        print(i)


print_mul_arg('pramod')
print_mul_arg(1, 2, 3, 4, 5)
print_mul_arg('sanjiva', 'pramod', 'ningayya')

import time


def greeting():
    print('Hello world')


greeting()


def greet():
    return "Hello Hello"


a = greet()
print(a)


def _greet(name):
    print(f"Hello {name}")


_greet('Deva')
_greet('Satya')


def _greet_someone(name):
    return f"hello {name}"


greet1 = _greet_someone('DJ')
greet2 = _greet_someone("John")
print(greet1, greet2)


def add_num(a, b):
    return  a + b

def _greet(name='World'):
    print(f"Hello {name}")

_greet('Pramod')
_greet("Trump")

def _greeting(name,age,pay):
    print(f"Your age is {age} and you are {name} and you get ${pay} salary")

_greeting('Pramod',35,10000)

# name, age and pay are called positional arguments
def greeting_(name, age = 28, salary = 100000):
    print(f"Hello {name} your age is {age} and your pay is {salary}")

greeting_("Pramod")
greeting_("George",40,2500000)

def greet(name, debug=False):
    if debug:      # If debug=True
        print("You have called greet function")
    else:
        print(f"Hello {name} how are you!")

greet("Hazel")
greet("Maria",True)






