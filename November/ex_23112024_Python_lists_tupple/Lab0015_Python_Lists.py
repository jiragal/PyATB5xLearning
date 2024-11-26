#PYTHON LISTS
# Lists are mutable
#Lists are collection of Items
# Element in the lists are ordered
# Lists can hold duplicates
# Lists can be indexed by integers starrting zero
# Lists are heterogeneous in nature but in Java array do not have different types of data list

# Creating an List
mylist = []
my_list = [1,2,3,4,5,8,4]
_mylists = list()    #Creating lists by using constructor
mylist_ = list('Sanjiva')       #Only argument is possible
mylib = ['Pramod',44,'Sandya','Shilpa','Rafi']
marks = [35,46,58,66,54,57]

fruits_ =['apple','guva','persimon','orange','grapes','banana']
print(fruits_)
_company_names = ['google','apple','microsoft','yahoo','amazon','instagram','ibm',]
print(_company_names)
_company_names.append('facebook')
print(_company_names)
print(fruits_[0])
print(len(fruits_))     #IF you try to access 7th element you will get "out of range" index
#Length starts from 1
#Index starts from 0
#Range starts from (Starts-pos,  end-position - 1)
for names in _company_names:       #Iterating the lists one by one
    print(names)

for i in range(1,6):
    print(i)



