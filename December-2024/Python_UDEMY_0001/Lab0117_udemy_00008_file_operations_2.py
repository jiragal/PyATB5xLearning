# Open the file read the file line by line
f = open("industry.csv", 'r')
data = f.readline()  # By default it will ready only first line
data1 = f.readline()
print(data)
print(data1)
f.close()

# Here we will learn how to append the file
f = open("simple.txt", 'w+')
data_write = f.write("We are learning Python language")
f.close()

#Here we will see appending data into file
f = open("simple.txt","a")
f.write("\n After that nodeJ")

