"""
Author: Fabio Daros
Date: 14.02.2024
"""

from typing import List
from time import sleep

from models.client import Client
from models.account import Account

accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print('================================')
    print('============= ATM ==============')
    print('========= Python Bank ==========')
    print('================================')
    print('Select an option: ')
    print('1. Create account')
    print('2. Make withdrawal')
    print('3. Make deposit')
    print('4. Make transfer')
    print('5. List accounts')
    print('6. Exit')

    option: int = int(input('Option: '))

    if option == 1:
        create_account()
    elif option == 2:
        make_withdraw()
    elif option == 3:
        make_deposit()
    elif option == 4:
        make_transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('See you later!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option!')
        sleep(2)
        menu()


def create_account() -> None:
    print('Enter customer details: ')

    name: str = input('Client name: ')
    email: str = input('Client email: ')
    number_identity: str = input('Client number identity: ')
    birth_date: str = input('Client birth date: ')

    client: Client = Client(name, email, number_identity, birth_date)

    account: Account = Account(client)

    accounts.append(account)

    print(f'Account {account.number} created!')
    print('Account details: ')
    print('--------------------------------')
    print(account)
    sleep(2)
    menu()


def make_withdraw() -> None:
    if len(accounts) > 0:
        account_number: int = int(input('Account number [WITHDRAW]: '))
        account: Account = search_account_by_number(account_number)
        if account:
            amount: float = float(input('Enter amount: '))
            account.withdraw(amount)
        else:
            print(f'Account {account_number} not found!')
        sleep(2)
        menu()
    else:
        print('There are no accounts!')
        sleep(2)
        menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        account_number: int = int(input('Account Number [DEPOSIT]: '))
        account: Account = search_account_by_number(account_number)
        if account:
            amount: float = float(input('Enter amount [DEPOSIT]: '))
            account.deposit(amount)
        else:
            print(f'Account {account_number} not found!')
    else:
        print('There are no accounts!')
    sleep(2)
    menu()


def make_transfer() -> None:
    if len(accounts) > 0:
        origin_number: int = int(input('Account number [TRANSFER]: '))

        origin_account: Account = search_account_by_number(origin_number)

        if origin_account:
            destination_account_number: int = int(input('Destination account number [TRANSFER]: '))
            destination_account: Account = search_account_by_number(destination_account_number)

            if destination_account:
                amount: float = float(input('Enter amount to transfer [TRANSFER]: '))
                origin_account.transfer(destination_account, amount)
            else:
                print(f'Account {destination_account_number} not found!')
        else:
            print(f'Account {origin_number} not found!')
    else:
        print('There are no accounts!')
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print('--------------------------------')
        print('Listing accounts:')
        print('--------------------------------')
        for account in accounts:
            print(account)
            print('--------------------------------')
            sleep(1)
    else:
        print('There are no accounts!')
    sleep(2)
    menu()


def search_account_by_number(number: int) -> Account:
    a: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.number == number:
                a = account
    return a


if __name__ == '__main__':
    main()
