import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")


def convert_amount_to_rub(transaction: dict) -> float:
    """Фукнция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    amount = transaction["operationAmount"]["amount"]
    currency_code = transaction["operationAmount"]["currency"]["code"]
    if currency_code not in ("USD", "EUR"):
        return float(amount)
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    headers = {"apikey": API_KEY}

    response = requests.get(url=url, headers=headers).json()
    return float(response["result"])
