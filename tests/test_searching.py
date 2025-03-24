import pytest

from src.searching import search_by_string


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
    "string, expected",
    [
        (
            "вклад",
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "description": "Открытие вклада",
                },
            ],
        ),
        (
            "счет",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод со счета на счет",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                    "description": "Перевод с карты на счет",
                },
            ],
        ),
    ],
)
def test_search_by_string(data, string, expected):
    assert search_by_string(data, string) == expected


def test_search_by_string_empty():
    assert search_by_string([]) == []
