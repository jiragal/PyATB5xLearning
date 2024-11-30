#  __init__ function
# Constructor --All class have function called __init__ function
#                   which is always executed when the object is being initiated.

#Creating class
class kids:
    name = 'karan'
    def __init__(self):
        print(self)
        print("Adding new student to the database")

#Creating object
s1 = kids()
print(s1.name)
s2 = kids()



