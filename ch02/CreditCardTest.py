import unittest

from ch02.CreditCard import CreditCard


class CreditCardTest (unittest.TestCase):
    def test_instantiation(self):
        cc = CreditCard("asis", "mybank", "1234567890", 1000)
        self.assertEqual("asis",cc.get_customer())
        self.assertEqual("mybank", cc.get_bank())
        self.assertEqual("1234567890", cc.get_account())
        self.assertEqual(1000, cc.get_limit())
        self.assertEqual(0, cc.get_balance())

    def test_many_credit_card(self):
        wallet = []
        wallet.append(CreditCard("asis", "mybank", "1234567890", 1000))
        wallet.append(CreditCard("John Bowman", "California Federal", "3485 03 99 3395 1954", 3500) )
        wallet.append(CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000) )

        for val in range(1, 17):
            wallet[0].charge(val)
            wallet[1].charge(2 * val)
            wallet[2].charge(3 * val)

        for c in range(3):
            print("Customer=", wallet[c].get_customer())
            print("Bank=", wallet[c].get_bank())
            print("Account=", wallet[c].get_account())
            print("Limit=", wallet[c].get_limit())
            print("Balance=", wallet[c].get_balance())
            while wallet[c].get_balance( ) > 100:
                wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
            print()
