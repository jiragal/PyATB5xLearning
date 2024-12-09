import os
#The os module in python provide functions for interacting with operating systems.
#The *os* and *os.path* modules include many functions to interact with the file system.
#Python os module functionality:
#                   *Handling the current working directory
#                   *Creating directoy
#                   *Listing out files with directory
#                   *Deleting files

# Getting the Current working directory(CWD) getcwd()
print(os.getcwd())

# Listing out Files and Directories with Python
files = os.listdir('/Users/91990/PycharmProjects/PyATB5xLearning/December-2024')
print(f"Current directory Lists: ", files)

#To print the name of the operating system
print(os.name)

# Creating a Directory
# os.mkdir("Python_File_Handling")  #In the current directly DIR will create




