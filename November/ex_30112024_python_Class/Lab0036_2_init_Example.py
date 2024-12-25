# To create class called Emp
# constructor : eid , ename, sal
# display() is another method inside class which will print eid, ename, sal


class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid     #We are converting local variable to class variable
        self.ename = ename
        self.sal = sal

    def display(self):
        print("Employee id is: ", self.eid)
        print("Employee name is: ", self.ename)
        print("The employee pay is: ", self.sal)


mc1 = Emp('IN00OXT406', 'pramod', 100000000)
mc1.display()

emp1 = Emp(456, 'david', 900000)
emp1.display()