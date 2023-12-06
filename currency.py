import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()


API_KEY = os.getenv('FREE_CURRENCY_API_KEY')
BASE_URL = f"{os.getenv('FREE_CURRENCY_BASE_URL')}{API_KEY}"

CURRENCIES = ["USD", "CAD", "SGD", "EUR", "AUD"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except KeyError as e:
        print(f"invalid currency {base}: {e}")
        return None


while True:
    base = input("Enter base currency (Q for quit): ").upper()
    if base == 'Q':
        break

    data = convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
