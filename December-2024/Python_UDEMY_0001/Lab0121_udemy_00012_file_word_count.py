#This Program illustrates word_count program
word_count = {}
with open("practice.txt", 'r') as f:
    data = f.read()
    data_split = data.split()
    print(data_split)
    for word in data_split:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

print(word_count)

# creating variable to store the
# Count number of words in file
number_of_words = 0
with open("greek.txt", 'r') as file:
    reading = file.read()
    lines = reading.split()
    print(lines)
    for item in lines:
        # checking if the word is numeric or not
        if not item.isnumeric():
            number_of_words += 1


# Printing total number of words
print(number_of_words)