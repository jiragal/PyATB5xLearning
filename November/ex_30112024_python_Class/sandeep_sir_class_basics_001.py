# class Parent(object):
#     def __init__(self, value):
#         self.value = value
#
#     def apple(self):
#         print('Parent.Apple', self.value)
#
#     def google(self):
#         print('Parent.Google')
#         self.apple()
#
#
# # Completely Independent Metho
# class Child1(Parent):
#     def yahoo(self):
#         print('Child1.Yahoo')
#
#
# # Overriding Parent class Method
# class Child2(Parent):
#     def apple(self):
#         print("Child2 Apple", self.value)
#
#
#
# # Overriding Parent class Method but reusing the original method in Parent
# class Child3(Parent):
#     def apple(self):
#         print("Child3 apple")
#         super().apple()
#
#
# obj_apple = Parent("Pramod")
# obj_apple.google()
#
# obj_child1 = Child1("tcs")
# obj_child1.yahoo()
#
# obj_child3 = Child3("amazon")
# obj_child3.apple()
# ************************2nd Page************************************************#
# Advanced Inheritance
class Parent(object):
    def spam(self):
        print('Parent Spam')


class Child1(Parent):
    def spam(self):
        print("Child1 spam")
        super().spam()


class Child2(Parent):
    def spam(self):
        print('Child2.Spam')
        super().spam()




# Multiple Inheritance Example
class Child3(Child1, Child2):
    pass


obj_1 = Child1()
#obj_1.spam()
obj_3 = Child3()
obj_3.spam()

# Multi-level inheritance, Here in this example method names are different, you can refer another Multilevel example
class A:
    def demo(self):
        print("A")

class B(A):
    def demo(self):
        print("B")
        super().demo()


class C(B):
    def demo(self):
        print("C")
        super().demo()

obj_c = C()
obj_c.demo()

# Overriding class variables
class Spami(object):
    a = 10
    def guva(self):
        print("guva",self.a)

class Peru(Spami):
    a = 20
    def orange(self):
        print("orange")
        super().guva()

obj_peru = Peru()
obj_peru.orange()















