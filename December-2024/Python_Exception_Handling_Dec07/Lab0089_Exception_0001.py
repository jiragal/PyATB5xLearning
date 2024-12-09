#Exception in Python are events occur during the execution of a program that disrupt
#normal flow of instructions.
#Name Error  2)Key Error 3) Value Error 4) Index Error 5)Type Error 6)Zero Division error etc
#Syntax Error
# print("Start the Program")
# a = int(input("Enter the num1"))
# b = int(input("Enter the num1"))
# c = a / b
# print("Result iv is: ", c)
# print("End of the Program")

#To fix the above Program by using try & except Block
print("Start the Program")
try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num1"))
    c = a / b
except Exception as e:
    print("Program is abend with: ", e)
print("End of the Program")

#Syntax
#try:
#       Try this code if something is error
#except:
    # Execute Something

#One more Example
import math
# print(math.exp(1000))   #OverflowError: math range error

#To fix the "OverflowError: math range error"
try:
    print(math.exp(1000))
except Exception as e:
    print("Program abend with", e)





