# Default Dict another example
# Counting occurances of each character in the string
from collections import defaultdict

s = 'abracadabraca'
s_count = defaultdict(int)
for char in s:
    s_count[char] += 1

print(s_count)

# Create a defaultdict with a default value of an empty list
my_dict = defaultdict(list)
print(my_dict)

#Add elements to empty dict
my_dict["fruit"].append("apple")
my_dict["fruit"].append("guva")
my_dict["fruit"].append("orrange")
my_dict["vegetable"].append("carrot")


print(my_dict)
