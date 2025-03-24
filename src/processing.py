from datetime import datetime

from src.widget import get_date


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Фильтрует список словарей по ключу state"""
    filter_data = []
    for elem in data:
        if elem["state"] == state:
            filter_data.append(elem)
    return filter_data


def sort_by_date(data: list, rev: bool = True) -> list:
    """Сортирует список по дате по убыванию"""
    for elem in data:
        value = elem['date']
        elem['date'] = get_date(value[:10])
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"), reverse=rev)
    return sorted_data


# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], rev=False))
# print(sort_by_date([]))
