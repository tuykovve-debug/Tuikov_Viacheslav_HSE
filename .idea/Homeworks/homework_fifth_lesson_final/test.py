import matplotlib.pyplot as plt

from Account import Account
from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount


def run_tests():
    account = Account("Иван Иванов")
    print(f"Номер счета: {account.account_number}")
    print(f"Баланс: {account.get_balance()}")

    account.deposit(5000)
    print(f"Баланс после пополнения: {account.get_balance()}")

    try:
        account.deposit(-100)
    except ValueError as e:
        print(f"Ошибка при пополнении: {e}")

    account.withdraw(200)
    print(f"Баланс после снятия: {account.get_balance()}")

    account.withdraw(1000)

    history = account.get_history()
    print("История операций:")
    for op in history:
        print(op)

    checking = CheckingAccount("Петр Петров")
    savings = SavingsAccount("Анна Смирнова", 1000)

    savings.deposit(500)
    savings.apply_interest(7)
    print(f"Баланс после начисления процентов: {savings.get_balance()}")

    savings.withdraw(400)
    print(f"Баланс после попытки снятия: {savings.get_balance()}")

    top_ops = savings.get_top_n_operations(2)
    print("Последние 2 крупные операции в сберегательном счёте:")
    for op in top_ops:
        print(op)

    account.plot_history()
    savings.plot_history()

    plt.show()


if __name__ == "__main__":
    run_tests()
