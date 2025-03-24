from collections import Counter

from src.file_read import func_read_file_csv


def group_by_categories(list_of_trans:list, list_categories:list)->dict:
    # Группировка данных по категориям
    dict = {}
    for elem in list_categories:
        count = Counter(elem.lower() in trans['description'].lower() for trans in list_of_trans)
        dict[elem] = count[True]
    return dict



if __name__ == "__main__":
  #  list_of_trans = func_read_file_csv("../data/transactions.csv")
    list_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "description": "Открытие вклада"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "description": "Перевод со счета на счет"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "description": "Перевод организации"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441", "description": "Перевод с карты на счет"}
    ]
    list_categories = ['перевод', 'деньги']

    result = group_by_categories({"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "description": "Открытие вклада"}, list_categories)
    print(result)



