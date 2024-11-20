# Create program to sum 3 numbers from the user input
# if user does not enter any number, use default values
def add_3_numbers(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

n1 = int(input('Enter input num1: '))
n2 = int(input('Enter input num2: '))
n3 = int(input('Enter input num3: '))

f1 = add_3_numbers()
f2 = add_3_numbers(1, 1, 1)
f3 = add_3_numbers(n1,n2,n3)
f4 = add_3_numbers(1000)

print(f1)
print(f2)
print(f3)
print(f4)
