# passing reference of one function to another function
def greet():
    return 'Hello World'

def spam(func):
    return func()

a = spam(greet)
print(a)
# 1. The reference of "greet" function is passed to "spam" function
# 2. "spam" function is invoking or executing "greet" function

def spmi(func):
    return func

b = spmi(greet)
print(b())   # invoking "greet" function
# both "b" and "greet" are pointing to same function object in the memory



