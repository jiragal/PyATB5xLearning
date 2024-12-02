class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance  # Public Variable
        self.__acount_number = account_number  # Private Variable

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        #print(self.__acount_number)


icici = Bank(9900503274, 100)
icici.deposit(100000)
print(icici.balance)
print(icici.check_balance())
