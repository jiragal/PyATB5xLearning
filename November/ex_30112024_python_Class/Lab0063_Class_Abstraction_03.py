# New Abstraction Example where we can see the hide things
from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def set_gear(self):
        pass


# Gerarbox get everything from Engine but Engine not
class Engine(GearBox):
    @abstractmethod
    def start(self):
        super().set_gear()
        pass

    @abstractmethod
    def stop(self):
        pass

#For the Car class "start" and "Stop" are hidden functionality
class Car(Engine):
    def start(self):
        print("Car starts durr...")

    def stop(self):
        print("Car stops...")

    def set_gear(self):
        print("Gear Box is ready")

    def drive(self):
        self.start()
        self.stop()
        self.set_gear()


# Object creating
obj_car = Car()
obj_car.drive()

#In the above example "Engine" Know about "Gear Box" and "Car" know about "Engone"
#Bye seeing Object Creating user dont know anything i.e hidding features from user
