#MultiLevel Inheritance
#Grand Father ---->Father ---->Son
class GrandFather:
    gold = "3KG"
    def bhk1(self):
        print("GrandFather has 1 BHK House only in Himachal Pradesh +", self.gold)

class Father(GrandFather):
    diamond = 'Kohinoor'
    def bhk2(self):
        print("Father has 2 BHK in Delhi")

class Child(Father):
    btc = "1BTC"
    def bhk3(self):
        print("Child has 3BHK House and Villa")

son = Child()
print(son.gold)     #Son accessing the GrandFather Property
print(son.btc)
print(son.bhk2())

appa = Father()
print(appa.gold)
# print(appa.btc)     #Father cannot access the son property




