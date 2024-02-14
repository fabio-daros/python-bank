"""
Author: Fabio Daros
Date: 14.02.2024
"""

from datetime import date
from datetime import datetime


def date_to_str(date_str: date) -> str:
    return date_str.strftime("%d/%m/%Y")


def str_to_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%d/%m/%Y")


def format_float_str_coin(value: float) -> str:
    return f"€ {value:0.2f}"

