#  __init__ function
# Constructor --All class have function called __init__ function
#                   which is always executed when the object is being initiated.

# Creating class
class kids:
    name = 'karan'
    """ Create a member from uname and fname """

    def __init__(self, name, mname, lname):
        self.name = name
        self.mname = mname
        self.lname = lname
        print(self)
        print("Adding new student to the database")


# Creating object
s1 = kids("pramod","dutta","maharaja")
print(s1.name,s1.mname,s1.lname)

