from collections import Counter


def group_by_categories(list_of_trans: list, list_categories: list) -> dict:
    """Группировка данных по категориям"""
    dict = {}
    for elem in list_categories:
        count = Counter(elem.lower() in trans["description"].lower() for trans in list_of_trans)
        dict[elem] = count[True]
    return dict
