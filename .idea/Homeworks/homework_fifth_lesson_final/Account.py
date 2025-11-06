from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


class Account:
    _account_counter = 1000

    def __init__(self, account_holder, balance=0):
        if not isinstance(account_holder, str) or not self._validate_name(account_holder):
            raise ValueError(
                "Имя владельца должно быть в формате 'Имя Фамилия' с загланых букв, кириллицей или латиницей")
        self.holder = account_holder
        self.set_balance(balance)
        self.account_number = f'ACC-{Account._account_counter}'
        Account._account_counter += 1
        self.operations_history = []

    def _validate_name(self, name):
        if not isinstance(name, str):
            return False
        parts = name.strip().split()
        if len(parts) != 2:
            return False
        for part in parts:
            if not (part[0].isupper() and part[1:].islower()):
                return False
        return True

    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Баланс должен быть > 0")
        self._balance = amount

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть > 0")
        old_balance = self._balance
        self._balance += amount
        self._add_operation('deposit', amount, old_balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть > 0")
        old_balance = self._balance
        if amount > self._balance:
            self._add_operation('withdraw', amount, old_balance, status='fail')
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        self._add_operation('withdraw', amount, old_balance)

    def _add_operation(self, operation_type, amount, prev_balance, status='success'):
        operation = {
            'type': operation_type,
            'amount': amount,
            'date': datetime.now(),
            'balance_after': self._balance,
            'status': status
        }
        self.operations_history.append(operation)

    def get_history(self):
        return self.operations_history

    def plot_history(self):
        df = pd.DataFrame(self.operations_history)
        if df.empty:
            print("Нет операцй для отображения")
            return
        df['date'] = pd.to_datetime(df['date'])
        df_sorted = df.sort_values('date')
        plt.figure(figsize=(10, 5))
        plt.plot(df_sorted['date'], df_sorted['balance_after'], marker='o')
        plt.title("История баланса по операциям")
        plt.xlabel("Дата")
        plt.ylabel("Баланс после операции")
        date_format = mdates.DateFormatter('%d-%m-%Y %H:%M')
        plt.gca().xaxis.set_major_formatter(date_format)
        plt.grid(True)
        plt.tight_layout()

        date_format = mdates.DateFormatter('%d-%m-%Y %H:%M')
        plt.gca().xaxis.set_major_formatter(date_format)

    def get_top_n_operations(self, n=5):
        sorted_ops = sorted(self.operations_history, key=lambda x: abs(x['amount']), reverse=True)
        return sorted_ops[:n]
