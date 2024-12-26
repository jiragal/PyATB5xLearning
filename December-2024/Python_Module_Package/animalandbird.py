# Here our requirement is to call the animal and bird module functions
# Approach1
print("1st Approach ******************************************")
import animal
import bird

animal.fly()
animal.color()

bird.fly()
bird.color()
print("2nd Approach ******************************************")
# 2nd Approach
from animal import *
fly()
color()
from bird import *
fly()
color()
print("3rd Approach ******************************************")