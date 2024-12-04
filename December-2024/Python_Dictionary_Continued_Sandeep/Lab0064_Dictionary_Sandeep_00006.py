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


