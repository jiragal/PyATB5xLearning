#In this program counting the number of words from file

# `open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
# on docs. python. org
count=[]
with open("GFG.txt", mode='r') as f1:
    for item in f1:
        for word in item.split():
            if word not in count:
                count.append(word)

print(len(count) + 1)    # counting the number of words from file
print(count)             # print the number of words in List





