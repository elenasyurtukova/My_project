import csv

import pandas as pd


def func_read_file_csv(path: str) -> list:
    """Функция: считывает данные из файла csv и возвращает список словарей транзакций"""
    try:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            list_of_transactions = []
            for row in reader:
                list_of_transactions.append(row)
            return list_of_transactions
    except FileNotFoundError:
        print("Файл не найден")
        return []


def func_read_file_excel(path: str) -> list:
    """Функция: считывает данные из файла excel и возвращает список словарей транзакций"""
    try:
        df = pd.read_excel(path)
        list_of_transactions = df.to_dict(orient="records")
        return list_of_transactions
    except FileNotFoundError:
        print("Файл не найден")
        return []


if __name__ == "__main__":
    print(func_read_file_csv("../data/transactions.csv"))
    # [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
    # 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
    # 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
    # 'description': 'Перевод организации'},
    # {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
    # 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
    # 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
    # 'description': 'Перевод с карты на карту'}]

    # print(func_read_file_excel("../data/transactions_excel.xlsx"))
    # [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
    # 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN',
    # 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
    # 'description': 'Перевод организации'},
    # {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
    # 'amount': 29740.0, 'currency_name': 'Peso', 'currency_code': 'COP',
    # 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
    # 'description': 'Перевод с карты на карту'}]
