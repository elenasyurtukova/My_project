from src.file_read import func_read_file_csv, func_read_file_excel
from src.processing import filter_by_state
from src.utils import get_transactions

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
