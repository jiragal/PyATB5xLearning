# An abstract class can be considered a blue print for other classes
# By default python does not have abstract classes.
# Python comes with a module that provides the base for defining Abstract Base Classes(ABC) and that module name is ABC
# ABC works by decorating methods of the base class.
# A method becomes abstract when decorated with the keyword @abstractmethod
# An abstract is need to hide the details
from abc import ABC, abstractmethod


class Animal(ABC):  # Here class is getting from ABC and this is how to add abstraction
    def __init__(self, name):
        self.name = name

    @abstractmethod  # Here it is incomplete method because we have no Idea
    def make_sound(self):
        pass


# In the above Animal(ABC) class we dont know which type of animal
class Dog(Animal):
    def make_sound(self):
        print("Bark Bark Bow Bow....")


# Object creating
obj_dog = Dog("Shera")
obj_dog.make_sound()

#Here question comes how exactly abstraction is added?
# Here in this example @abstract method is hidden and it is enforced into the next class

