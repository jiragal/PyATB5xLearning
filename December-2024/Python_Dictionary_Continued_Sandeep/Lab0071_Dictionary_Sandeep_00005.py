# Counting number of characters in a string
s = 'abracadabraca'
char_count = {}
letter_count = {}
for item in s:
    if item in char_count:
        char_count[item] += 1
    else:
        char_count[item] = 1

print(char_count)

# 2nd-Way
s = 'abracadabraca'
for count in s:
    letter_count[count] = letter_count.get(count,0) + 1

print(letter_count)
