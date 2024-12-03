# MultiPle Class
class Father:
    def father_money(self):
        return 10


class Mother:
    def mother_money(self):
        return 5


class Son(Father, Mother):
    def get_son_info(self):
        print("Son can access both Father and Mother money")

s = Son()
print(s.father_money())
print(s.mother_money())

#Multiple Inheritance concept is there in Python not in JAVA


    

