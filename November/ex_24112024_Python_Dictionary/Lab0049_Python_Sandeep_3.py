# points
points = {'a': 1, 'b': 2, 'c': 3}
# Incrementing value of key 'a
points['a'] = points['a'] + 1
points['a'] += 1
print(points)

#Adding new key value pair
points['d'] = 4
print(points)
#Adding multiple records
points.update({'e':5,'f':6})   #here we are adding multiple records
print(points.items())  # Returns a tuple of key,value pairs
#Print only key of the dictionary
for item in points:
    print(item)

for key,value in points:
    print(key,value)
