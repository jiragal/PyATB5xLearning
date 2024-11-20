# Usage of **args--This means passing numbers of arguments i. unlimited numbers of arguments you can pass
def print_mul_arg(*args):
    for i in args:
        print(i)


print_mul_arg('pramod')
print_mul_arg(1, 2, 3, 4, 5)
print_mul_arg('sanjiva', 'pramod', 'ningayya')
