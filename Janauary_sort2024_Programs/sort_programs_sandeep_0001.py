# sorted method returns a new list in sorted order.
#Original list or tuple or dictionary remains there

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'micrsoft','carelon']
numbers=(8,3,5,0,1,4,7,3,9,2,10)
share_prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20,'FB':105.00}
word='hello how are you'

names_sort=sorted(names)
name_sorted=sorted(names,reverse=True)  # sorts the list in descending order
print(names)
print(names_sort)
print(name_sorted)

# Sotring strings
word = "helloworld"
print("".join(sorted(word)))    #convert the list to string

# SORTING TUPLES
sorted_numbers= sorted(numbers)
print(sorted_numbers)

# Sorting Dictionary
# Sorts the keys of the dictionary in ascending order
sorted_dict=sorted(share_prices)
print(sorted_dict)




