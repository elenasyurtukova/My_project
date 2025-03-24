import re


def search_by_string(list_of_dict: list, search_string: str = "Перевод") -> list:
    """Функция фильтрует список словарей по строке в описании"""
    filtered_list = []
    str_search = search_string.lower()
    for trans in list_of_dict:
        match = re.search(str_search, trans["description"].lower())
        if match is not None:
            filtered_list.append(trans)
    return filtered_list


if __name__ == "__main__":
    #   print(search_by_string([]))
    print(
        search_by_string(
            [
                {
                    "id": "650703",
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": "16210",
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                },
                {
                    "id": "3598919",
                    "state": "EXECUTED",
                    "date": "2020-12-06T23:00:58Z",
                    "amount": "29740",
                    "currency_name": "Peso",
                    "currency_code": "COP",
                    "from": "Discover 3172601889670065",
                    "to": "Discover 0720428384694643",
                    "description": "Перевод с карты на карту",
                },
            ],
        )
    )
