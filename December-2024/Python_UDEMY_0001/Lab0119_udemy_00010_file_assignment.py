#Create file "practice.txt" add the following data in it
#1st Step
# with open("practice.txt",'w') as f:
#     f.write("Hi Everyone\nwe are learning File I\O\n")
#     f.write("Using Java.\nI like programming in Java.")
#     f.close()

#2nd Step
with open("practice.txt",'r') as fo:
    data = fo.read()
    new_data = data.replace("Java", "Python")
    print(new_data)
    fo.close()

#3rd Step
with open("practice.txt", 'w') as wo:
    wo.write(new_data)
    wo.close()



