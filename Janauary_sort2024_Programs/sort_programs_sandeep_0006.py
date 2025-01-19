# Find the longest sub-string in the below string

sentence = "This is a Programming language and Programming is fun"
words=sentence.split()
print(words)

#1st way is Loop technique
max_length= 0

for item in words:
    if len(item) > max_length:
        max_length = len(item)

print(max_length)

#2nd way is max() function
# Use max() with key=len to find the word with the maximum length
longest_length= len(max(words,key=len))
print(longest_length)

#3rd ways is: Using list comprehension
longest_word= max([len(item) for item in words])
print(longest_word)

#4th ways is: Using list comprehension along with sort method ***This one is very important***

d_lengthy_word= {word:len(word) for word in words}
print(d_lengthy_word)
longest_wording= sorted(d_lengthy_word.items(),key=lambda item:item[-1])
print(longest_wording)
print(longest_wording[-1])

