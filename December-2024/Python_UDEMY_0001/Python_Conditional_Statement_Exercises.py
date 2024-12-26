#1 Mark Even and Odd - Python
# Input: x = 4
# Output: Even
def checkOddEven(x1):
    if x1 % 2 == 0:
        return True
    else:
        return False

check = checkOddEven(10)
print(check)
#********************************************************************************************#
# Given two integer variables a and b, and a boolean variable flag.
# The task is to check the status and return accordingly.


def check_status(a, b, flag):
    if (a>0 and b<0 and flag == False):
        return True
    elif(a<0 and b<0 and flag == True):
        return True
    else:
        return False


chk = check_status(-1,1,True)
print(chk)
