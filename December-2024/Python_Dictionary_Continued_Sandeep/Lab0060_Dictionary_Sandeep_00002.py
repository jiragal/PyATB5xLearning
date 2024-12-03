# points
points = {'a': 1, 'b': 2, 'c': 4}

# Incrementing value of key 'a'
points["a"] = points['a'] + 1
points['a'] += 1
# Adding a new key value pair
points['d'] = 1
points['d'] += 2

print(points.items())
print(points.values())
#printing Key-Value
for item, value in points.items():
    print(item, value)

for item in points:    #Printing only key
    print(item)

for item in points:         #Printing only Value
    print(points[item])

for item in points.keys():  #Printing only key
    print(item)

for item in points.values():
    print(item)