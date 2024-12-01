# Encapsulation simple project with "CAR"
class Car:
    def __init__(self, o_name, o_model, o_make):
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def start_engine(self):
        print("Starting engine with car name: ", self.name)
        print("Starting engine with model name: ", self.model)
        print("Starting engine with car_making_year: ", self.make)


lamb = Car("Lamborgani", "V6", 2024)
print(lamb.start_engine())
bwm = Car("BMW","BMW_SAFARI",2023)
print(bwm.start_engine())