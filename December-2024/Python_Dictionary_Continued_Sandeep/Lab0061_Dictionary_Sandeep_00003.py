# Count number of words in a sentence --word count program
sentence = 'helo world how the world is growing in 21st century, is it world is changing'
words = sentence.split()
word_count = {}
for item in words:
    if item in word_count:
        word_count[item] += 1
    else:
        word_count[item] = 1

print(word_count)

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
# word count program and here input is LIST items
vowels = ['a', 'e', 'i', 'o', 'i', 'u', 'a', 'e', 'e']
my_vowels = " ".join(vowels)  #Converting lists into String and then count the items
item_count = {}
for item in my_vowels:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1


print(item_count)