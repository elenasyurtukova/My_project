import os
import json
import requests
from dotenv import load_dotenv

def info_transaction(transaction:dict)->float:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях"""
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        result = float(transaction['operationAmount']['amount'])
    else:
        amount = float(transaction['operationAmount']['amount'])
        currency_code = transaction['operationAmount']['currency']['code']

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        load_dotenv(dotenv_path='../.env')
        API_Key = os.getenv('API_Key')
        payload = {}
        headers = {
            "apikey": API_Key
        }
        response = requests.get(url, headers=headers, data=payload)
        result = round(response.json()['result'],2)
    return result

if __name__=='__main__':
    print(info_transaction({
        "id": 854048120,
        "state": "EXECUTED",
        "date": "2019-03-29T10:57:20.635567",
        "operationAmount": {
            "amount": "30234.99",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Classic 1203921041964079",
        "to": "Счет 34616199494072692721"
    }))


