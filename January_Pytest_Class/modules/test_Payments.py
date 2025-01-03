#test_Payments.py
import pytest

class TestPayments:
    def test_paymentinDollars(self,setup):
        print("This is payment in DollarMethod")
        assert True == True

    def test_paymentinRupees(self,setup):
        print("This is payment in RupeesMethod")
        assert True == True