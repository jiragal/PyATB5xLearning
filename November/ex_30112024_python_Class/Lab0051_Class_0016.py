#Private attributes and methods
#Private attributes and methods are meant to be used only within the class
#and are not accessible from outside the class.
class Account:
    def __init__(self,account_num,password):
        self.account_num = account_num      #Public variable
        self.__password = password          #Private variable

    def res_password(self):
        print(self.__password)

#Now will create object and print the account information
# acc1 = Account(9900503274, "Pass1234")
# print(acc1.account_num)
# print(acc1.password)

#This time we will create one more object acc2
acc2 = acc1 = Account(9900503274, "Pass1234")
print(acc2.account_num)
print(acc2.res_password())
print(acc2.__password)                     #We will get error because password is now private







