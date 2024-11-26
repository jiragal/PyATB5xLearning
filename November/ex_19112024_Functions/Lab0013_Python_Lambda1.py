def _add_numbers(a, b, c):
    return a + b + c

result = _add_numbers(1, 3, 5)
print(result)

result1 = lambda a, b, c: a + b + c
print(result1(2, 3, 5))

result3 = lambda num: num ** 2
print(result3(2))

def add(n):
    return n + 10

print(add(2))

add = lambda n: n + 10
print(add(2))
print(add(10))
# passing multiple arguments
mul = lambda a,b: a*b
print(mul(2,3))

#Passing multiple argumants
add = lambda a,b,c: a+b+c
print(add(2,5,90))

#Ternary operators in lambda
check_odd_even = lambda num:"even" if num%2 == 0 else "odd"
given =check_odd_even(18)
given1 = check_odd_even(19)
print(given)
print(given1)

c_even_odd = lambda *args: 'even' if args%2 == 0 else "odd"
list1 =[1,3,5,6,7,8,22]
list2 =[]
for i in list1:
    #Use lambda to check given number is odd or even
    chk =lambda i: "even" if i%2 == 0 else 'odd_number'
    list2.append(chk(i))
print(list2)








