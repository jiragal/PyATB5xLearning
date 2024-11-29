#To find missing key
dict1 = {'a': 1, 'b':2, 'c':3}
dict2 = {'a': 1, 'b':2}

missing_key = set(dict1.keys()) - set(dict2.keys())
print(missing_key)

#Sort a dictionary by its values in descending order
input_dict = {'Math': 90, 'DSA': 80, 'Algo': 95, 'Python': 75}
#Assignment
