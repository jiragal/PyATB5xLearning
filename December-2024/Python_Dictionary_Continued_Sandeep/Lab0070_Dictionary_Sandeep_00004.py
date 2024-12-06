# Count number of words in a sentence
sentence = 'hello world hello world welcome to python'
words = sentence.split()
word_count = {}
for item in words:
    word_count[item] = word_count.get(item,0) + 1

print(word_count)

months = ['January', 'February', 'March']
count_dict = {}
for item in months:
    count_dict[item] = count_dict.get(item,0) + 1

print(count_dict)

#Initialize an empty dict
#Iterate througn each item in a List
#Use the .get(key,default) method to get the current count of the item
#Default is zero(0) if item is not in the dict
#The dictionary count_dict will store the count of each unique item in the list








