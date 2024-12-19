#Unpacking Packed values
#Unpacking is the act of splitting the packed value into individual variable contained in a list or tuple
#swapping variable
a = 10
b = 20
#Traditional approach
tmp = a
a = b
b = tmp
#Swapping done

#using unpacking swapping
a,b = b, a

d = {'p': 1, 'y': 2, 't': 3, 'h': 4}
for item, value in enumerate(d):
    print(item,value)

l = [1,2,3,4,5,6]

print(l[0])

a,b = l[0],l[1:]
print(b)

#Usage with Ordered Type, once we unpack we will get results in LIST
a1, *b = [-10,1,5,7]
print(a1)
print(b)

#From tuple if we unpack we will get LIST
a2, *h = (210,1,25,79)
d1 = {'p','y'}
d2 = {'t','h','n'}
d3 = {'o','n','h'}
d = (*d1,*d2,*d3)    #Unpacking in tuple format contains duplicate item
print(d)
d = [*d1,*d2,*d3]   #Unpacking in LIST format contain duplicate
print(d)
d = {*d1, *d2, *d3}  #Unpacking of item without duplicate items
print(d)

#To unpack in dictionary we should use ** operator
d1 = {'p':1,'y':2}
d2 = {'t':3,'h':4,'o':5}
d3 = {'n':6,'h':7}
d = {**d1, **d2, **d3}
print(d)

#Nested Unpacking
l = [1,2,[3,4]]
a,b,c = l
print(f"a={a} b={b} c={c}")
d,e = c
print(d)
print(e)

s = 'python'
a,b,c,d = s[0],s[1],s[2:-1] ,s[-1]      #Unpacking in Slicing way
*c, = c    #Another way is list(c)
print(a, b, c, d)
#Now we can unpack of string to list

#Joining two lists
l1 = [1,2,3]
l2 = [4,5,6]
l = l1 + l2      #Another way is: l = [*l1, *l2]
print(l)
l = [*l1, *l2]
print(l)

#Define Function with *args parameter
def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count
    # if count == 0:
    #     return 0
    # else:
    #     return total / count

average = avg(10,20,30,40,50)
print(average)
print(avg())




















