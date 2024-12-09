# In This program showing we can add multiple exception
try:
    num1 = int(input("Enter num1 \n"))
    num2 = int(input("Enter num2 \n"))
    result = num1 / num2
    print(result)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Output results is: ", result)
finally:
    print("This code will always execute wether program succesful or fail")
