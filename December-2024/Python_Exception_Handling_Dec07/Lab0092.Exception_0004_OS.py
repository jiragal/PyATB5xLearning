import os
from fileinput import close

#To check file existed or not?

check_file_path = os.path.exists('TestData.txt')
print(check_file_path)

try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path + "/TestData.txt"
    print(full_path_file)

#To read the file
#file.open("path or name of the file"),mod)
#mod = r,w,x
    file = open(full_path_file)
except Exception as e:
    print("File not found fix the path or create file", e)
finally:
    file.close()
    print("File closed successfully")
