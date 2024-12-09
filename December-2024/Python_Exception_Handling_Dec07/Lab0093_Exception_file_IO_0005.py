#Writing new file
import os
file_name = "pramod.txt"
content = 'This is pramod File abc'

#write
with open(file_name,"w") as file:
    file.write(content)

#open file
with open(file_name,"r") as file:
    content2 = file.read()
    print(content2)

#move file to desktop
# os.rename("TestData.txt","/Desktop/TestData.txt")