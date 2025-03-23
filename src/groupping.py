from collections import Counter

import pandas as pd

from src.file_read import func_read_file_csv


def group_by_categories(list_of_trans:list, list_categories:list)->dict:
    # Группировка данных по категориям
    dict = {}
    for elem in list_categories:
        count = 0
        for trans in list_of_trans:
            if trans['description'] == elem:
                count += 1
        dict[elem] = count
    return dict



# if __name__ == "__main__":
#     list_of_trans = func_read_file_csv("../data/transactions.csv")
#     list_categories = []
#     for trans in list_of_trans:
#         if trans['description'] not in list_categories:
#             list_categories.append(trans['description'])
#
#     result = group_by_categories(list_of_trans, list_categories)
#     print(result)



