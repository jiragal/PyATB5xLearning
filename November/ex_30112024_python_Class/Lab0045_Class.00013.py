# Global vs Private
class PrintGlobal:
    def __init__(self):
        self.password = "pramod"   #Public Instance Variable
        self.__password_secure = "Pwd1234"  #Private Variable

    def change_pwd(self):
        print(self.password)
        print(self.__password_secure)  #Private variable we can print because it is within the class so we can use


object_ref = PrintGlobal()
print(object_ref.password)
chg = object_ref.password = "Pass1234"
print(chg)

object_ref1 = PrintGlobal()
print(object_ref1.password)
print(object_ref1.__password_secure)
