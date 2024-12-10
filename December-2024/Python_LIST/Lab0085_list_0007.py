# reverse():
# It is used to reverse the order of elements in the list.
num2 = [1,2,3,4,5,6,7,8,9,10]
num2.reverse()
print(num2)

# ********************************************************************************************************#
#sort()
#In list by default insertion order is preserved.
# If you want to sort the elements of list according to default natural sorting order then we should go for
#  sort() method.
# For numbers ==> default natural sorting order is Ascending Order
# For Strings ==> default natural sorting order is Alphabetical Order

n=[20,5,15,10,0]
n.sort()
print(n)
# ********************************************************************************************************#
# To use sort() function, compulsory list should contain only homogeneous elements, otherwise we will get
#  TypeError.
str1 = ["Dog","Banana","Cat","Apple"]
str1.sort()
print(str1)
# ********************************************************************************************************#