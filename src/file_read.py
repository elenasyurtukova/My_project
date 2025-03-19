import csv
import pandas as pd

def func_read_file_csv(path: str) -> list:
    """Функция: считывает данные из файла csv и возвращает список словарей транзакций"""
    try:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
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
        list_of_transactions = df.to_dict(orient='records')
        return list_of_transactions
    except FileNotFoundError:
        print("Файл не найден")
        return []



if __name__ == "__main__":
    print(func_read_file_csv("../data/transactions.csv"))
    # print(func_read_file_excel("../data/transa_ctions_excel.xlsx"))
