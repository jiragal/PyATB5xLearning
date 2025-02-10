#Python program to Count the Number of occurrences of a key-value pair in a text file


#Open a file
with open("file3.txt",mode='r') as file3:
    d= dict()
    for item in file3:
        items = item.strip()
        it = items.lower()
        lines = it.split()
        print(lines)
        for line in lines:
            if line in d:
                d[line] = d[line] + 1
            else:
                d[line] = 1

file3.close()

print(d)
for key in list(d.keys()):
    print(f"The count of {key} is {d[key]}")




