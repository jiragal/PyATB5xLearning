class Person:
    __name = "anonymous"
    def __helo(self):
        print("Hello Person")

    def wellcome(self):
        self.__helo()

p1 = Person()
print(p1.wellcome())
p1.__hello()
