class Rectangle:
    def __init__(self, width, height):    #Instance Methods
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height             #Instance Methods

    def perimeter(self):
        return 2 * (self.height + self.width)

    #String representation is doing here
    def to_string(self):
        return "Rectangle: width={0}, height={1}".format(self.width, self.height)

    def __str__(self):    #Override Methods
        return "Rectangle: width={0}, height={1}".format(self.width, self.height)

    def __repr__(self):   #Override Methods
        return "Rectangle ({0},{1})".format(self.width, self.height)

    #Here r1 object will use "self" and r2 will use "other" r1 == r2 here 2 object we are comparing
    def __eq__(self, other):  #Override Methods
        if isinstance(other, Rectangle):  #Here we are saying other is instance of Rectangle
            return self.width == other.width and self.height == other.height
        else:
            return False


r1 = Rectangle(10, 100)
print(r1.area())
print(r1.perimeter())
print(r1.to_string())
print(str(r1))
print(repr(r1))        #Our results will display in different format
r2 = Rectangle(10,10)
pr = r1 is not r2
print(pr)

print(r1 == r2)
print(r1 == 100)     #Because of if isinstance(other, Rectangle):

var1 = 10
print(hex(id(var1)))




