# Lambda Expression and Functions
# Lambda is anonymus function that retruns some form of data.
def add(a, b):
    return a + b


def func(a, b):
    return a ** 2 + b ** 2 + 2 * a * b


def func2(a, b, c):
    return 2 * a + 3 * b + 4 * c


def last(item):
    return item[-1]


def find_even_odd(num):
    if num % 2 == 0:
        print('The given number', num)
    else:
        print("The number is Odd")


# For the above 4 Function now we will try to create Labmbda Functions
add = lambda a, b: a + b
print(add(100, 250))

func = lambda a, b, c: a ** 2 + b ** 2 + 2 * a * b
print(func(10, 10, 10))

func2 = lambda a, b, c: 2 * a + 3 * b + 4 * c
print(func2(10, 10, 10))

last = lambda item: item[-1:]
print(last('Pramod'))

find_even_odd = lambda num: "even" if num % 2 == 0 else "The number is Odd"
print(find_even_odd(99))
print(find_even_odd(100))
