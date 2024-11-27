from itertools import zip_longest

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# Iterating through the List (pythonic approach)
for item in names:
    print(item)

# Prints the item and its corresponding index in the list (Pythonic approach)
my_list=['Ronald','John','Alex','Ravi']
for index, item in enumerate(my_list):   # enumerate returns a tuple of index,
    print(index, item)

# Using range function (not preferred method)
for index in range(0, len(names)):
    print(names[index])
# **********************************************************************************
# Printing alternate items of the list (Pythonic approach)
num3 = [1,2,3,4,5,6,7,8,9,10]
for num in num3[::2]:
    print(num)
#Same logic will use range method
for num in range(0, len(num3),2):
    print(num)
# **********************************************************************************
#We can print only Item or Index
for index,item in enumerate(names):
    print(item)

for index, item in enumerate(names):
    print(index)
# **********************************************************************************
# Index always starts from 0 but we can change this manually
for index, item in enumerate(names, start=1):
    print(index, item)
# **********************************************************************************
city_list = ['Bangalore','Hoodi','Rajajinagar','Banashankari','RajaRajeshwari']
city_pincode =[560002,560048,560010,560050,560098]

# Iterating through multiple list Non-Pythonic approach
for item in range(len(city_list)):
    print(city_list[item],city_pincode[item] )
# Iterating through multiple list by uzing zip method()
for index, item in zip(city_list,city_pincode):
    print(index, item)
# **********************************************************************************
# Iterating through multiple list with un-equal lengths using zip function
a= [1,2,3]
b = ['v','w','x','y','z']

for index, item in zip(a,b):
    print(index, item)           # zip function stops at the shortest list

for i, j in zip_longest(a,b):
    print(i,j)

for x,y in zip_longest(a,b,fillvalue='NA'):
    print(x, y)
# **********************************************************************************#
a = [1,2,3]
b = ['x','y','z']
c = ['alpha','beta','gamma']

for item in zip_longest(a,b,c):
    print(item)
#Both are Same?
for i,j,k in zip(a,b,c):
    print(i,j,k)
# **********************************************************************************#
files = ['youtube.txt','amazon.pdf','facebook.pdf','google.pdf','apple.doc']
for file in files:
    if file.endswith('pdf'):
        print(file)
    else:
        print("File Not Found")
# OR OR#
for file in files:
    if file[-3: ] == 'pdf':
        print("The pdf file name is:", file)
    else:
        continue
# **********************************************************************************#
#  Multiple conditions in startswith and endswith function
# Need to change above logic in different way
filenames = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.py', 'apple.doc']
for file in filenames:
    if file.endswith(('txt', 'pdf')):
        print(file)
# **********************************************************************************#
# Converting Lists to String
print("_".join(filenames))
print("|".join(files))
print(",".join(files))
# **********************************************************************************#
# Slicing List's
# names[start:stop:step]
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'micrsoft']
#          0         1         2        3         4             5            6
#         -1        -2        -3       -4        -5            -6           -7
print(names[0:])
print(names[0:2])        #start =0 stop=stop-1
print(names[3:1])        #This will not work and not give any error
print(names[2:5])        # Prints all the items from 2nd index upto but not include 5th one
print(names[:4])         # Prints all items from 0th index and upto 4th index, but
print(names[2:])         # Prints all items from 2nd index till the end of the List
print(names[1 + 3])      # Prints 4th item of the list   Single Item is printed
print(names[1 - 3])      # Prints 5th item of the list
print(names[0])
# **********************************************************************************#




























