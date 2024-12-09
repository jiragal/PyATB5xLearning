# pop(): ----->It removes and returns the last element of the list.
# This is only function which manipulates list and returns some element.
# If the list is empty then pop() function raises IndexError.
# In general we can use append() and pop() functions to implement stack datastructure by using list,which
# follows LIFO(Last In First Out) order.

n1 = [10, 20, 30, 40, 50]
n1.pop()  # By default last elment will be removed
n1.pop(0)  #  to remove elements based on specified index.
print(n1)

# append(),insert(),extend() ===>for increasing the size/growable nature
# remove(),pop() ======>for decreasing the size /shrinking natur
# List objects are dynamic (i.e., based on our requirement we can increase and decrease the size).