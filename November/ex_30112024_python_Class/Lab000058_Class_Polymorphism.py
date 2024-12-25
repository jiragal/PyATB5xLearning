# Polymorphism in Python
# Polymorphism refers to having multiple forms.
# Polymorphism is programming term that refers to the use of same function name:
# but with different signatures, for multiple types.
# Example Pramod in his home behaves differently infront of his wife and his mother
# Example of in-built polymorphic functions:
# Behaviour is different based on who is calling
# Two types of Polymorphism
#           Method overriding
#           Method overloading

# Method Overloading Example  ----Same name(function name but different arguments)

class Dog:
    def _bark(self):
        print("Dog is barking")

    def _bark(self, breed):
        print(f"Dog with {breed} is barking")


d = Dog()


# 2nd Example "Method Overloading"
class MathUtil:
    def add(self, a=0, b=0):
        return a + b

    def add(self, a=2, b=4, c=5):
        return a + b + c

    def add(self, a=4, b=4, c=3, d=0):
        return a + b + c + d


math = MathUtil()
op1 = math.add(1,1)
op2 = math.add(6, 9, 99)
op3 = math.add(1, 2, 23, 45)
print(op1,op2,op3)