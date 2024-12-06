# Counting number of vowels in a string
word = 'hello world welcome to python'
vowels = 'aeiou'
v_count = {}
for item in word:
    if item in vowels:
        if item in v_count:
            v_count[item] = v_count[item] + 1
        else:
            v_count[item] = 1

print(v_count)

# 2nd way
word =word.lower()
# Define vowels
vowels = 'aeiou'
#Count the number of vowels in the string
vowel_count = sum(1 for char in word if char in vowels)  #This logic is important
print(vowel_count)



