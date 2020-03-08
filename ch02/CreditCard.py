class CreditCard:
    """ A consumer credit card """
    def __init__(self, customer, bank, account, limit):
        """ Creates a new card instance

            The initial balance is zero

            customer    the name of customer (eg. asis)
            bank        the name of bank (eg; sbi)
            account     the account identifier (eg 1234567890)
            limit       credit limits measured in dollars
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """ Return name of customer """
        return self._customer

    def get_bank(self):
        """ Return name of bank """
        return self._bank

    def get_account(self):
        """ Return account identiifier """
        return self._account

    def get_limit(self):
        """ return current limit of the card """
        return self._limit

    def get_balance(self):
        """ return balance of the card """
        return self._balance

    def charge(self, price):
        """ return true if charge was processed; otherwise false """
        if (price + self._balance) > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """ processes customer payment; reduces balance """
        self._balance -= amount
