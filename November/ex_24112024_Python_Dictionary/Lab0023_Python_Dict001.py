from collections import OrderedDict
from collections import defaultdict

# Different ways of constructing a dictionary
d = {}
d1 = dict()
d2 = dict(Bangalore=25, Chennai=34, Kolacutta=38)
d3 = dict([('Bangalore', 23), ('Madras', 45), ('Hyderabad', 50)])
d4 = dict({'emp001': 'Sanjiva', 'Emp002': 'Pramod', 'Emp003': 'Sharat'})
d5 = dict(zip(['RRNagar', 'Hoodi', 'MGRoad'], [560098, 570099, 567300]))

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


