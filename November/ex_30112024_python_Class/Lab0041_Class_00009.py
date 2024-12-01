# Lets practice
# Create Account class with 2 attributes Balance and account number
# Create method for debt and credit and printing the balance

class Account:
    def __init__(self, bal, accn):
        self.balance = bal
        self.account_no = accn

    # Create debt method
    def debt(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print("total balance:> ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print("total balance:> ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debt(1000)
acc1.credit(500)
acc1.credit(40000)   #Salary

