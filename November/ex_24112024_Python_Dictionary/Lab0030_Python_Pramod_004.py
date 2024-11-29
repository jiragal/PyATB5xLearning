#To find frequency of a character in a string
# string = input('Enter the name')
# count_char = {}
# for char in string:
#     if char in count_char:
#         count_char[char]  = count_char[char] + 1
#     else:
#         count_char[char] = 1

# print(count_char)
#Another way is
count_occr_char = {}
name = input("Enter user name: ")
for item in name:
    count_occr_char[item] = count_occr_char.get(item, 0) + 1

print(count_occr_char)




