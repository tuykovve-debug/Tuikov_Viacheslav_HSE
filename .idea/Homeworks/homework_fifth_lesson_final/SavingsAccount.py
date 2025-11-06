from Account import Account


class SavingsAccount(Account):
    account_type = 'Savings'

    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)

    def apply_interest(self, rate):
        if rate < 0:
            raise ValueError("Процентная ставка должна быть > 0")
        interest = self._balance * (rate / 100)
        old_balance = self._balance
        self._balance += interest
        self._add_operation('interest', interest, old_balance)
        return interest

    def withdraw(self, amount):
        if amount > self._balance * 0.5:
            raise ValueError("Нельзя снять боле 50% от остатка.")
        super().withdraw(amount)
