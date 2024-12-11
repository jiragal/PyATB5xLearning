# Combining both
from numpy.ma.core import remainder


def anyargs(*args,**kwargs):
    print(args)        #return tuple
    print(kwargs)      #return dictionary

anyargs(1,25,100,name='sandeep',city='Bangalore')

# =======================================================================#
#Unpacking arguments List
def unpack(name,age,salary):
    print(f"Hello {name} you are become {age} year old and your salary is {salary}")

list_item = ['pramod','32','50Lakh']
unpack(list_item[0],list_item[1],list_item[2])
# greet(*data) # Equivelent to greet("Steve", 26, 1000)
d_data = {"name": "steve", "age": 26, "pay": 1000}
unpack(d_data['name'],d_data['age'],d_data['pay'])
# greet(**d_data) # Equivelent to greet(name="Steve", age=26, pay=1000)
# =======================================================================#
# Returning Multiple Values from a Function
def div(a,b):
    r = a%b
    q = a/b
    return r, q

remainder, quatent = div(4,2)
print(remainder)
print(quatent)
