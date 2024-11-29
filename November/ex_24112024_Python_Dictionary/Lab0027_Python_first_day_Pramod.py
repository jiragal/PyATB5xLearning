# Tradinal way of dict is defining in this way
# Dict is generally useful in API-TESTING with JSON
my_dict = {
    "name": 'Aman',
    "age": '35',
    "role": 'SDET',
    "experience": 3
}
#Another way of creating dict
student_infor2 =    dict(name='Pramod',age=29,role='SCRUM MASTER',experience = 12)
# Accessing dict elements
print(my_dict["age"])
# Updating Values
my_dict['experience'] = 5
print(my_dict)

#Deleting the elements
del my_dict['role']
print(my_dict)

#Iterating the dict item
for key, values in my_dict.items():
    print(key, " ===>",values)

#To know the which are the methods in dict
print(dir(my_dict))
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

