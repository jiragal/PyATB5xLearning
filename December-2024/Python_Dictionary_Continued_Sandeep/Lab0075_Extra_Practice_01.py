# 1. Creats a key if the key does not exist
# 2. Initialise the value to empty list in case of defaultdict of list
# 3. Returns the empty list
from collections import defaultdict

profile = defaultdict(list)
profile['language'].append("java")
profile['language'].append("Python")

print(profile)

cities = [('India', 'Bangalore'),
          ('India', 'Chennai'),
          ('India', 'Delhi'),
          ('India', 'Kolkata'),
          ('USA', 'Dallas'),
          ('USA', 'New York'),
          ('USA', 'Chicago'),
          ('China', 'Bejing'),
          ('China', 'Shaingai')
          ]
print(type(cities))
dd = defaultdict(list)
dd1 = { }
for country, city in cities:
    dd[country].append(city)

print(dd)

#Try to write to dictionary
