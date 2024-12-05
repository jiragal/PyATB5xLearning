# One more example for Abstract method
from abc import ABC, abstractmethod


class Father:
    def __init__(self, father):
        self.father = father

    # Your father has incomplete Loan
    @abstractmethod
    def loan(self):
        pass


class Son:
    def loan(self):
        print("1Lakh given to ICICI loan cleared")


# Object creating
obj_loan = Son()
obj_loan.loan()

#Abstract means hidden but in this example we cannot see that..Pramod has explained that in the next program
