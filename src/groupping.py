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
    list_of_trans = func_read_file_csv("../data/transactions.csv")
    list_categories = ['перевод', 'вклад', 'счет']

    result = group_by_categories(list_of_trans, list_categories)
    print(result)



