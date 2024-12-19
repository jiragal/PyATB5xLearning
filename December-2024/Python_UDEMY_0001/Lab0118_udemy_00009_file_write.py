# Creating a File using the write()
#Here file was not present but run time "greek.txt"
file = open("greek.txt", 'w')
file.write("This is the write command")
file.write("\nIt allows us to write in a particular file")
file.close()

# Example 2: We can also use the written statement along with the  with() function.
with open("file.txt", 'w') as f:
    f.write("Hello pramod how are you!")
    f.close()

#Working of Append Mode
# Python code to illustrate append() mode
with open("greek.txt", 'a') as f:
    f.write("\nThis will add to the file")
    f.close()

# #context manager with
# with open("access-log.txt") as f:
#     for line in f:
#         print(line)
#     f.close()

##context manager with
#Here we are reading the "access-log.txt"
#Writing all the ip-address to the LIST
ip = []
f = open("access-log.txt",'r')
for line in f:
    parts = line.split()
    ip.append(parts[0])
print(ip)

#Here we are counting the ip-address occurrence in dictionary format
count = {}
for item in ip:
    if item in count:
        count[item] += count[item]
    else:
        count[item] = 1

#Here we are sorting ip=address values based on specified key
most_frequent_ip = sorted(count.items(), key=lambda item : item[-1])
print(most_frequent_ip)
most_frequent_ip = dict(most_frequent_ip)
print(most_frequent_ip)
#print(count)
f.close()