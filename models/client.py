"""
Author: Fabio Daros
Date: 14.02.2024
"""

from datetime import date
from utils.helper import date_to_str, str_to_date


class Client:
    counter: int = 101

    def __init__(self, name: str, email: str, number_identity: str, birth_date: str) -> None:
        self.__code: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__number_identity: str = number_identity
        self.__birth_date: date = str_to_date(birth_date)
        self.__registered_date: date = date.today()
        Client.counter += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def number_identity(self: object) -> str:
        return self.__number_identity

    @property
    def birth_date(self: object) -> str:
        return date_to_str(self.__birth_date)

    @property
    def registered_date(self: object) -> str:
        return date_to_str(self.__registered_date)

    def __str__(self: object) -> str:
        return (f"Code: {self.__code} \nName: {self.__name} \nBirth Date: {self.__birth_date} "
                f"\nRegistered Date: {self.__registered_date}")
