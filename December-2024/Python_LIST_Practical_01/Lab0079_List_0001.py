from itertools import zip_longest

# LISTS Theory
"""
1. Lists are Mutable
2. Elements in the Lists are Ordered
3. Lists can hold duplicate elements
4. Lists can be indexed by integers starting zero
5. Lists are heterogeneous in nature. (They can point to any kind of objects)
"""
my_lists = []
my_lists1 = [1, 2, 3, 4, 5]
my_list = list()  # By using the list constructor
list1 = list("helloworld")
list2 = list([1, 2, 3, 4, 5])

# Creation of list object With dynamic input:
list = eval(input("Enter List:"))
print(list)
print(type(list))

# Creation of list object With dynamic input:
list1 = eval(input("Enter the list"))
list2 = list(list1)
print(list2)
