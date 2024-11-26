import math


def mathpow(num):
    return math.pow(num, 2)


op = mathpow(2)
print(op)
# Same code will implement with Lambda

math_pow = lambda: math.pow(int(input("enter num\n")), 2)
print(math_pow())
