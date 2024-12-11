from time import sleep, time


# A decorator is a function which adds some extra function without modifying to the existing function
def make_pretty(func):
    def wrapper():
        print("I got decorated")
        func()

    return wrapper

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

