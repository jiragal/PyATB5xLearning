"""
1) The tuples are Immutable
2) Elements in the tuples are ordered
3) Tuples can be indexed by integers starting zero
4) Tuple are heterogeneous in nature - They can point to any index
"""
from os import remove

# Creating tuple
t = ()  # Creating empty object
t1 = tuple(['hero', 'trump', 'kia', 'tata', 'bmw'])  # Using tuple constructor
sports = ('hockey', 'cricket', 'kabaddi')
t2 = (1,)  # Single Item tuple
t3 = (1, 8, 3, 4, 6,)
print(t1)
new_tuple = (t1, t3)  # Creating new tuple within tuple
print(new_tuple)
# Python Access Tuple using a Positive Index
print(new_tuple[1][1])
fresh_tuple = (t1, sports)
print(fresh_tuple[0][0])

# Real time example
cities = ('London', 'Paris', 'Washington', 'Tokyo', 'Japan', 'Russia')
print('America' in cities)
print('Japam' in cities)
t = (1, 2, 3, 4, 5)
# tuple are indexed
print(t[1])
print(t[2])
#Tuple contains duplicate
tp1 = (1,2,3,3,4,2,3)
print(tp1)
remove_duplicate = set(tp1)
print(remove_duplicate)

#'tuple' object does not support item assignment ---Immutable
    # tp1[0] = 100
    # print(tp1)
# Like List Traversal, we can traverse through a tuple using for loop.
for item in tp1:
    print(item )

# Concatenation of Python Tuples
t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')

t3 = t1 + t2
print(t3)

# Nesting of Python Tuples
t4 = (t1, t2)
print(t4)              #A tuple inside another tuple







