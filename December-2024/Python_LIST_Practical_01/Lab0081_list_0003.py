# Important functions of List:  list()
list_1 = list(range(1,11))
print(list_1)
# **************************************************************************************
#lin() Function   :- It returns the number of elements present in the list.
print(len(list_1))
# **************************************************************************************
#count()   :>  It returns the number of occurrences of specified item in the list.
num_list = [1,2,3,1,3,4,2,5,6,4,7,8,1]
print(num_list.count(4))
# **************************************************************************************
# index(): :>>>>It returns the index of first occurrence of the specified item.
# If the specified element not present in the list then we will get ValueError.
print(num_list.index(4))
print(num_list.index(4,2))

l = [10,20,30,40,10,20,10,10]
user_number = int(input('Enter value to search : '))
if user_number in l:
    print(user_number,'available occurent at : ',l.index(user_number))
else:
    print("User number is not available", user_number)



