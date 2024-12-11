def add_sprinkles(func):
    def wrapper():
        print("You add sprinkles")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("You add fudge")
        func()
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream():
    print("Here is your icecream")


get_ice_cream()
