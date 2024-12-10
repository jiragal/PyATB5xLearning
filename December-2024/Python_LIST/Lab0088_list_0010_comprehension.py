# List comprehension
# Names starting with consonents
list1 = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'evilia', 'anup', 'ivan', 'om']
consonants_list = [item for item in list1 if item[0] not in 'aeiou']
print(consonants_list)
# **************************************************************************************#
# Filtering out those names which are less than 6 characters
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
names_len = [item for item in names if len(item) < 6]
print(names_len)
# **************************************************************************************#
# Raise to the power of list index
a = [1, 2, 3, 4, 5]
pow = [values ** key for key, values in enumerate(a)]
print(pow)
# **************************************************************************************#
# Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail']
str_len_pair = [(name,len(name)) for name in names]
print(str_len_pair)
# **************************************************************************************#
# Build a list of tuples with string and its length pair
names1 = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail']
even_string = [item for item in names1 if len(item)%2 == 0]
print(even_string)
# **************************************************************************************#
# Reverse the item of a list if the item is of odd length string
names2 = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail']
reversed_list = [item[::-1] for item in names2 if len(item)% 2 != 0]
print(reversed_list)
#Another way
def process_name(name):
    if len(name) % 2 == 0:
        return name
    else:
        return name[::-1]

reverse_odd_length = [process_name(name) for name in names]
print(reverse_odd_length)
# **************************************************************************************#
data = ['hello', 123, 1.2, 'world', True, 'python']
d = [item[::-1] if isinstance(item, str) else item for item in data]
print(d)
# **************************************************************************************#
# Reverse the string if the string is of odd length, otherwise keep it as is.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail','amazon']
odd_list1 = [name[::-1] if len(name)% 2 !=0 else name for name in names]
print(odd_list1)
# **************************************************************************************#








