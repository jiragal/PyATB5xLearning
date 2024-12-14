#Argument vs Parameter

#The 'a' and 'b' are called as parameter
def add(a,b):
    return a+b

obj1 = add(10,100)     #Here for 'a' and 'b' we call argument we are passing

x, y = 5, 15
obj1(x,y)
#'x' & 'y' are called as arguments
#Also note that x & y are passed by reference
#i.e memory addresses of 'x' and 'y' are passed



