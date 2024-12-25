# In the below example we are showing Local/Global/Class Variable
i, j = 10, 20     #Global Variable


class Myclass:
    a, b = 100, 200   #Class Variable

    def add(self, x, y):
        print(self.a + self.b)
        print(x + y)
        print(i + j)


mc = Myclass()
mc.add(1, 2)

#Example 5: we are creating variable with same  name
g, k = 10,20
class Mychoice:
    g, k = 100,200
    def magi(self,g,k):
        print("Local variable: ",g+k)
        print("class Variable: ", self.g * self.k)
        print("Global Variable: ",globals()['g'] + globals()['k'])


mc2 = Mychoice()
mc2.magi(1,2)












