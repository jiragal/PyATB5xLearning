# How to sort the elements of list in reverse of default natural sorting order?
n=[40,10,30,20]
n.sort()
print(n)
n.reverse()
print(n)

#2nd Way is
n1=[40,10,30,20]
n1.sort()
n1.sort(reverse=True)
print(n1)

# Aliasing and Cloning of List objects:
x=[10,20,30,40]
y = x
print(y)
# The problem in this approach is by using one reference variable if we are changing content,then those
# changes will be reflected to the other reference variable.
y[0] = 100
print(x)
print(y)

#slicing i) List slicing:
# list2 = list1[start:stop:step]
# start ==>it indicates the index where slice has to start default value is 0
# stop ===>It indicates the index where slice has to end default value is max allowed index of list ie length
# of the list
# step ==>increment value (step default value is 1)
l = [10,20,30,40,50,60]
print(l[0:3:])
#
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])     #3,5,7
print(n[4::2])      #5,7,9
print(n[3:7])       #4,5,6,7
print(n[8:2:-2])    #9,7,5
print(n[4:100])     # 5,6,7,8,9,10





