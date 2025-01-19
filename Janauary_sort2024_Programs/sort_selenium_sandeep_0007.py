# Find the longest non-repeating sub-string in the below string
sentence = "This is a Programming language and Programming is fun"
words= sentence.split()
new_words=[]

#By using loop function first removed repetitive word
for item in words:
    if words.count(item) == 1:
        new_words.append(item)

print(new_words)
longest_word= len(max(new_words,key=len))
print(longest_word)

#now find longest non-repeating substring
max_len= 0

for item in new_words:
    if len(item) > max_len:
        max_len= len(item)
        lengthy_word = item

print(lengthy_word)

#2nd ways is List comprehension and sorted method
d= {item: len(item) for item in words if words.count(item) == 1}
longest_non_repeating_word = sorted(d.items(),key=lambda item:item[-1])
print(longest_non_repeating_word[-1])





