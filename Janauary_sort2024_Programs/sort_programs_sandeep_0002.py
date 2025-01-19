# Custom Sorting
cmp_names=['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'micrsoft','lowes','carelon']
cmp_names.append('zentech')
#Based on length of items sorting will happen
print(sorted(cmp_names,key=len))

# Sorting the list based on the last character of the list item
#We will use both sorted() and Lambda----Syntax> lambda arguments: expression
items = ['bv', 'aw', 'dt', 'cu','ba','zb']
items_result = sorted(items,key=lambda item:item[-1])
print(items_result)

#Sort the list items based on city temperatures
temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai',38),('Rajasthan',45)]
temp_results=sorted(temperatures,key=lambda item:item[-1])
print(temp_results)  #By default, it will display results in ascending order
