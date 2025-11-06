from Account import Account


class CheckingAccount(Account):
    account_type = 'Checking'

    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
