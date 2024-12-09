# Create File and write one line record
import os

#If file not exist it will create and write "Hello" if you run one more time it will keep on add records
with open("Amit.txt", "a") as file:
    file.write("Hello")
