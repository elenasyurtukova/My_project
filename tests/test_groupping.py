import pytest

from src.groupping import group_by_categories


@pytest.fixture()
def data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "description": "Открытие вклада"},
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод со счета на счет",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "description": "Перевод с карты на счет",
        },
    ]


@pytest.mark.parametrize(
    "list_categories, expected_list",
    [
        (["Перевод", "Вклад", "Счет"], {"Перевод": 3, "Вклад": 1, "Счет": 2}),
        (["вклад", "Счет"], {"вклад": 1, "Счет": 2}),
        (["перевод", "деньги"], {"перевод": 3, "деньги": 0}),
    ],
)
def test_group_by_categories(data, list_categories, expected_list):
    assert group_by_categories(data, list_categories) == expected_list


def test_group_by_categories_empty():
    assert group_by_categories([], ["перевод", "деньги"]) == {"перевод": 0, "деньги": 0}
    assert group_by_categories(data, []) == {}
    assert group_by_categories([], []) == {}
