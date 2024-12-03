# Count number of words in a sentence
setence = 'helo world how the world is growing in 21st century, is it world is changing'
words = setence.split()
word_count = {}
for item in words:
    if item in word_count:
        word_count[item] += 1
    else:
        word_count[item] = 1

print(word_count)