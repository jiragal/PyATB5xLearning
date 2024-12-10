# append():
# We can use the append() function to add the item at the end of the list
# By using this append function we always add the element at the end of the list

# Write a Python Program to add all elements to list upto 100 which are divisible by 10.

list_1 = list(range(0, 101))
list2 = []

for item in list_1:
    if item % 10 == 0:
        print(item, "Even number and is divisible by 10", list2.append(item))

print(list2)
# Another Way:
list3 = []
for item in range(0,101,10):
    list3.append(item)

print(list3)


#Result ----->>> [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# **************************************************************************************#
