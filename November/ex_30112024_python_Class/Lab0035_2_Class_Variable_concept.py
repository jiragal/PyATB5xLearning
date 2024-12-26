# Class Variable demonstration
#How to create class variable & How to access those variables
class VariableClass:
    a, b = 100, 200  # 'a' & 'b' are Local Variable

    def add(self):
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)


mc = VariableClass()
mc.add()
mc.mul()
