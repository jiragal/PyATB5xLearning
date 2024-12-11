# 1.filter() function:
# We can use filter() function to filter values from the given sequence based on some condition.
# For example, we have 20 numbers and if we want to retrieve only even numbers from them.

#Syntax :>  filter(function,sequence)
    #Where,
        # 1)function argument is responsible to perform conditional check.
        #2)sequence can be list or tuple or string.

list_num = [0,5,10,20,30,40,50,60]
# Program to filter only even numbers from the list by using filter() function
def findEven(x):
    if x%2 == 0:
        return True
    else:
        return False
even_list = list(filter(findEven,list_num))
print(even_list)

#We can try same thing with Lambda Function
l = [22,8,7,4,3,33,0,1,6,77]
find_even = list(filter(lambda x:x%2 ==0,l))   #As per syntax he has choose parameters
print(find_even)


