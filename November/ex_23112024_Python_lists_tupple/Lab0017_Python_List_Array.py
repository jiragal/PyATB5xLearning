names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# Iterating through the List (pythonic approach)
for item in names:
    print(item)

# Prints the item and its corresponding index in the list (Pythonic approach)
my_list=['Ronald','John','Alex','Ravi']
for index, item in enumerate(my_list):   # enumerate returns a tuple of index,
    print(index, item)

# Using range function (not preferred method)
for index in range(0, len(names)):
    print(names[index])

