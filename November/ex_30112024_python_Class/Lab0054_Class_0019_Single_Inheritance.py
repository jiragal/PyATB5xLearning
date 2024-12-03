class Father:
    apartment = "2BHK"
    gold = "3KG"

    def bhk2(self):
        print(self.apartment)


# Child Class
class Child(Father):
    diamond = "Diamond"

    def bhk3(self):

        print("3BHK")


child_object = Child()
print(child_object.gold)      #Child accessing the father property
print(child_object.bhk2())

father_object = Father()
father_object.bhk2()
# father_object.bhk3()     #Father cannot access the child property
