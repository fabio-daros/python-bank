"""
Author: Fabio Daros
Date: 14.02.2024
"""

from models.client import Client
from utils.helper import format_float_str_coin


class Account:
    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.code
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self.calculate_total_balance
        Account.code += 1

    def __str__(self: object) -> str:
        return (f"Account Number: {self.__number} \nClient: {self.__client} "
                f"\nTotal Balance: {format_float_str_coin(self.__total_balance)}")

    @property
    def number(self: object) -> int:
        return self.__number

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self: object) -> float:
        return self.__total_balance

    @property
    def calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, amount: float) -> None:
        pass

    def withdraw(self: object, amount: float) -> None:
        pass

    def transfer(self: object, destination_account: object, amount: float) -> None:
        pass
