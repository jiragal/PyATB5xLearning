# First Program how to create DICT
# Different ways of constructing a dictionary
from collections import OrderedDict
from collections import defaultdict
d1 = {}
d2 = dict()
d3 = dict(Bangalore=25, Mysore=40)
d4 = dict([("Maths", 89), ("Physics", 90), ("Chemistry", 97), ("Biology", 95)])
d5 = dict(zip(["high", "medium", "low"], [55, 32, 22]))
d6 = dict({'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'})

print(type(d5))
for item, value in d4.items():
    print(item, value)
print(d4["Maths"])   #Accessing Values of dict
print(d6.get('apple'))   #By using "get" method

# Adding / Updating the dictionary
d4["Biology"] = 99      #Updating the value
d4["English"] = 92      #Adding new element to the list
print(d4)
# Adding / Updating the dictionary
# list inside the dictionary as values.
location = {'country': 'India', 'states': ['Karnataka', 'Anrda', 'Kerala']}
location['states'].append("Maharastra")
print(location)










