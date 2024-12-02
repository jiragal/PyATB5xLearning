from collections import OrderedDict
from collections import defaultdict

# Different ways of constructing a dictionary
d = {}
d1 = dict()
d2 = dict(Bangalore=25, Chennai=34, Kolacutta=38)
d3 = dict([('Bangalore', 23), ('Madras', 45), ('Hyderabad', 50)])
d4 = dict({'emp001': 'Sanjiva', 'Emp002': 'Pramod', 'Emp003': 'Sharat'})
d5 = dict(zip(['RRNagar', 'Hoodi', 'MGRoad'], [560098, 570099, 567300]))

#Exmple with City and ZIP codes#
d = {}
print(d)
d1 = dict()  #Empty
print(d1)
d2 = dict(Audugod=560030,RajaRajeshwari=560098)
print(d2)
d3 = dict([("Anekal",562106),("Bangalore City",56002)])
print(d3)
d4 = dict(zip(["Ashoknagar","Bannerghatta"],[560050,560083]))
print(d4)
d5 = dict({"Basaveshwaranagar":560079,"Chickpet":560053})
print(d5)
print(len(d5))
print(d5["Basaveshwaranagar"])
print(d5.get("Chickpet"))

"""
DICT
Key and value pair
A dictionary is an unordered mutable and indexed and collection of key value pairs in Python
Where it will be used: API Automation(JSON,DICT)
Dictionary are mutable
"""
print(d5['RRNagar'])  # Accessing Dict Elements my_dict[key]
# Adding or updating key-value pair
d5['Hoodi'] = 560048
print(d5)
del d3['Hyderabad']
print(d3)
# Iterating Dict
for index, item in d4.items():
    print(f"The emp_id:{index} and their names:{item}")


