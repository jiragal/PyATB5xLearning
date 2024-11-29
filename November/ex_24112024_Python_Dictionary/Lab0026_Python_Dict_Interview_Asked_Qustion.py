#Program to ream the string and count the number of charcters into dictionary
string = input('Enter the string ex automation')
count_string = {}
for char in string:
    if char in count_string:
        count_string[char] += 1
    else:
        count_string[char] = 1

print(count_string)

#Anoter way
char_count ={}
string = 'python'
for char in string:
    char_count[char] = char_count.get(char,0) + 1   #Here we are using get method
print(char_count)

vowels_args = 'aeiou'
string = 'python'
my_list = []
for char in string:
    if char not in vowels_args:
        my_list.append(char)
    else:
        print('Vowels are:', char)

print(my_list)
single_element = ''.join(my_list)
print('Consonants are: ', single_element)  # Output: "python"

