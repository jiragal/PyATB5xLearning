from itertools import zip_longest
num = [1, 3, 5, 7, 8, 3, 9.2]
print(num)
num1 = [0, 99, 100, 22, 11, 10]
num.extend(num1)  # extend  method used
print(num)
s = set(num)  # set method is used to remove duplicate and result we get it in dict
print(s)
# Inster method we will try
num1.insert(1, 33)
num1.insert(2, 'pramod')  # insert 'pramod' at postion 2
print(num1)
num1.insert(6, 'sanjiva')
print(num1)
lis = ['Welcome', 'Scaler']
lis.insert(1, 'to')
print('List:', lis)
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']
names.append('sandisk')  # append will add record at end
print(names)
print(dir(names))
# Comment ************************************
# We will use extend() method
names.extend(['netflix', 'walmart', 'kroger'])  # Here also it will add record at end
print(names)
# Comment ************************************
# We will see how to merge two lists
a = ['apple', 'gmail', 'coco-cola']
b = ['amazon', 'netflix', 'microsoft']
d = ['sandisk', 'dell', 'lenovo']

c = a + b
print(c)
# another way of merging is
e = [*a, *b, *d]
print('sandisk' in e)  # Checking value is exist in List or Not
# Comment ************************************
# Removing Items from the List
names.remove('kroger')  # Remove items from the list
names.pop()  # Remove last item from the list
print(names)
names.pop(3)
print(names)
# pop method returns the item that it has removed from the List
# Comment ************************************
#Deletes the item from the list
del names[0]   #Deletes 0th Item from the List
# del names[3:6]   #Delete the Item from 3, 4, 5 item in the list
# del names[::2]   #Delete the alternate item in the list
# del names       # Deletes the reference to the list "names"
# del names       #Delete the entire list
# Comment ************************************
# Making copy of the list (Shallow Copy!!!)
a = [1,2,3,4,5]
b = a.copy()
print(b)
# OR
c = a[:]
print(c)
# Comment ************************************
# 6_Sorting List's
names = ['Hello','Rahul','Anand','Sagar','Manish','Pramod','Zydus','Babu']
print(names)
names.sort()                # Sorts the List in Alphabetical Order
print(names)
new_names = sorted(names)
print(new_names)
my_list=['Ronald','John','Alex','Ravi']
my_list.sort(reverse=True)  # Sorts the List in Decending Order
print(my_list)
sorted(my_list, reverse=True) # Sorts the List in Decending Order
print('David' in my_list)  # Returns True if the item present in the List





















