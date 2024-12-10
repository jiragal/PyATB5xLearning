# insert():  >>> It is used to insert item at specified index position.

number_s = [1, 2, 3, 4, 5, 6, 8]
number_s.insert(0, "numbers")
print(number_s)

n = [1, 2, 3, 4, 5]
n.insert(10, 777)
n.insert(-10, 999)
print(n)
print(n.index(777))
print(n.index(999))

# If the specified index is greater than max index then element will be inserted at last position.
# If the specified index is smaller than min index then element will be inserted at first position.

# extend():  ---->If we waant to add all items of one list to another list,we use extend() method.

order1 = ["Chicken", "Mutton", "Fish"]
order2 = ['KF', 'BF', 'FO']
num1 = [0, 4, 3, 2, 5, 6, 9, 90]
order1.extend(order2)
print(order1)
# Anotehrh way
new_number_list = number_s + num1
print(new_number_list)

l2 = [40, 50, 60]

l2.extend(num1)
print(l2)

# remove():
# We can use this function to remove specified item from the list.
# If the item present multiple times then only first occurrence will be removed
# If the specified item not present in list then we will get ValueError.
n = [10, 20, 10, 30]
n.remove(10)
print(n)
# Hence before using remove() method first we have to check specified element present in the list or not by
#  # using in operator.
l1 = [10, 20, 30, 40, 50, 60, 70]
x1 = 60
if x1 in l1:
    l1.remove(x1)
else:
    print("Item is not available", x1)

print(l1)   #We can see the 60 is removed