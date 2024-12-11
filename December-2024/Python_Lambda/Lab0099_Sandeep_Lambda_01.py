# lambda expressions/functions
def add(a,b):
    return a+b
def  squareIt(n):
    return n*n

def findNum(a,b):
    if a>b:
        print("The a is big number",a)
    else:
        print("The b is a big number")

# print(findNum(100,10))

#Corresspnding Lambda Program
# lambda expressions or ananoymous functions
# lambda args_list: expression
# By using Lambda Functions we can write very concise code so that readability of the program will be improved.

# Write a program to create a Lambda function to find sum of 2 given numbers
add = lambda a,b : a + b
fadd = add(4,10)
print(fadd)

# Write a program to create a lambda function to find square of given number
squareIts = lambda n: n*n
print(squareIts(10))

# Write a program to create a Lambda Function to find biggest of given values.
s = lambda a,b:a if a>b else b
print("The Biggest of 10,20 is:",s(10,20))
print("The Biggest of 100,200 is:",s(100,200))