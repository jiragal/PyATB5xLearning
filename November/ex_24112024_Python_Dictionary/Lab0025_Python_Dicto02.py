# Dictionary from two list
key = {'name', 'role', 'experience'}
values = {'Aman', 'SDET', '3'}
my_dict = dict(zip(key, values))
print(my_dict)

#Merging two dict
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}

dict3 = dict1 | dict2      # to merge + operator will not works 
