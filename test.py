"""
Author: Fabio Daros
Date: 14.02.2024
"""

from models.client import Client
from models.account import Account

client_1: Client = Client('Client 1', 'client_1@email.com', 'YB099833', '02/09/1987')
client_2: Client = Client('Client 2', 'client_2@email.com', 'YB067754', '10/03/2000')

account_1: Account = Account(client_1)
account_2: Account = Account(client_2)

print(account_1)
print(account_2)