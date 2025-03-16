import json


def get_transactions(path:str)->list[dict]:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as data_file:
            try:
                transactions_data = json.load(data_file)
                return transactions_data
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []

if __name__=='__main__':
    print(get_transactions('../data/operations.json'))
