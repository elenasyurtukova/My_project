import datetime

from src.file_read import func_read_file_csv, func_read_file_excel
from src.processing import filter_by_state, sort_by_date
from src.searching import search_by_string
from src.utils import get_transactions
from src.widget import get_date, mask_account_card
from collections import defaultdict
from datetime import datetime

def main():
    """Функция основной логики проекта: взаимодействие с пользователем"""
    punkt = int(input('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n'''))

    if punkt == 1:
        print("Для обработки выбран JSON-файл")
    elif punkt == 2:
        print("Для обработки выбран CSV-файл")
    elif punkt == 3:
        print("Для обработки выбран XLSX-файл")

    while True:
        status_user = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n''')
        status = status_user.upper()
        if status in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Операции отфильтрованы по статусу {status_user}')
            break
        else:
            print(f'Статус операции {status_user} недоступен.')

    if punkt == 1:
        data_of_trans = get_transactions("../data/operations.json")
    elif punkt == 2:
        data_of_trans = func_read_file_csv("../data/transactions.csv")
    elif punkt == 3:
        data_of_trans = func_read_file_excel("../data/transactions_excel.xlsx")
    filtered_transactions = filter_by_state(data_of_trans, state = status)
    print(filtered_transactions)

    filter_date = input('Отсортировать операции по дате? Да/Нет\n')
    if filter_date.lower() == 'да':
        filtered_transactions_date = sort_by_date(filtered_transactions)
    else:
        for trans in filtered_transactions:
            new_date = get_date(trans['date'])
            trans['date'] = new_date
        filtered_transactions_date = filtered_transactions
    print(filtered_transactions_date)

    filter_amount = input('Отсортировать по возрастанию или по убыванию\n')
    if filter_amount.lower() == 'по возрастанию':
        sorted_transactions = sorted(filtered_transactions_date, key=lambda trans: trans['amount'])
    else:
        sorted_transactions = sorted(filtered_transactions_date, key=lambda trans: trans['amount'], reverse=True)
    print(sorted_transactions)

    filter_currency = input('Выводить только рублевые тразакции? Да/Нет\n')
    if filter_currency.lower() == 'да':
        transactions_cur = []
        for trans in sorted_transactions:
            if trans['currency_code']  == 'RUB':
                transactions_cur.append(trans)
    else:
        transactions_cur = sorted_transactions
    print(transactions_cur)

    filter_string = input('Отфильтровать список транзакций по определенному словy в описании? Да/Нет\n')
    if filter_string.lower() == 'да':
        string_for_filter = input('Введите слово для фильтрации, иначе отфильтруем "Переводы"\n')
        if string_for_filter.lower() != "перевод" and len(string_for_filter) > 0:
            transactions_filtered_string = search_by_string(transactions_cur, string_for_filter)
        else:
            transactions_filtered_string = search_by_string(transactions_cur, 'перевод')
    else:
        transactions_filtered_string = transactions_cur
    print(transactions_filtered_string)


    len_list = len(transactions_filtered_string)
    if len_list > 0:
        print(f'Всего банковских операций в выборке: {len_list}')

        for trans in transactions_filtered_string:
            date = trans['date']
            operation = trans['description']
            sum = trans['amount']
            cur_name = trans['currency_name']
            mask_to = mask_account_card(trans['to'])
            if 'from' in trans.keys() and trans['from'] != '' and type(trans['from']) == str:
                mask_from = mask_account_card(trans['from'])
                print(f'''{date} {operation}
{mask_from} -> {mask_to}
Сумма: {sum} {cur_name}
                    ''')
            else:
                print(f'''{date} {operation}
{mask_to}
Сумма: {sum} {cur_name}
                        ''')
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

if __name__=='__main__':
    main()


