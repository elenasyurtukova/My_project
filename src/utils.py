import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    encoding="UTF-8",
    filemode="w",
)
logger = logging.getLogger("utils")


def get_transactions(path: str) -> list[dict]:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info(f"Обращаемся к файлу {path}")
        with (open(path, encoding="utf-8") as data_file):
            try:
                transactions_data = json.load(data_file)
                new_transactions_data = []
                for trans in transactions_data:
                    if trans != {}:
                        value_amount = trans["operationAmount"]["amount"]
                        value_currency_name = trans['operationAmount']['currency']['name']
                        value_currency_code = trans['operationAmount']['currency']['code']
                        del trans["operationAmount"]
                        trans['amount'] = value_amount
                        trans['currency_name'] = value_currency_name
                        trans['currency_code'] = value_currency_code
                        if 'from' in trans.keys():
                            trans = {'id':trans['id'], 'state':trans['state'], 'date':trans['date'],
                                    'amount':value_amount, 'currency_name': value_currency_name,
                                    'currency_code': value_currency_code, 'from':trans['from'],
                                    'to':trans['to'], 'description':trans['description']}
                        else:
                            trans = {'id': trans['id'], 'state': trans['state'], 'date': trans['date'],
                                     'amount': value_amount, 'currency_name': value_currency_name,
                                     'currency_code': value_currency_code, 'to': trans['to'],
                                     'description': trans['description']}
                        new_transactions_data.append(trans)
                    else:
                        continue
                logger.info("Данные о финансовых транзакциях получены")
                return new_transactions_data
            except json.JSONDecodeError:
                logger.error("Произошла ошибка декодирования файла")
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logger.error("Произошла ошибка: файл не найден")
        print("Файл не найден")
        return []


if __name__ == "__main__":
    print(get_transactions("../data/operations.json"))
    # print(type(get_transactions("../data/operations.json")))

    # [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
    # 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
    # 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
    # {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
    # 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
    # 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]

# csv, xlsx
    # [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
    # 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
    # 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
    # 'description': 'Перевод организации'},
    # {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
    # 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
    # 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
    # 'description': 'Перевод с карты на карту'}]
