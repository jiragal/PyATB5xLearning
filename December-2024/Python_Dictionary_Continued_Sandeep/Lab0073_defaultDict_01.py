# defaultDict
# Python defaultDict is a container like dictionaries present in the module collections.
# Functionalities of both defaultDict amd Dict are same but for defaultDict never raise keyError
# Creates key if does not exists.
# Initiate the value to zero in case of defaultdict of int's
# Returns the value to zero
from collections import defaultdict

# Counting occurances of word in the string
sentence = "hello world welcome to python hello hi hello hello"
sentence = sentence.lower()
#Now use split method and result will be in list and then we will count the words
word = sentence.split()
word_count = defaultdict(int)
char_count = {}
for words in word:
    word_count[words] += 1

print(word_count)

#Normal Dict Method
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


print(char_count)



