import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [(7000792289606361, '7000 79** **** 6361'),
                                                   (4530639492982, 'Ошибка, неверно введен номер карты'),
                                                   ('60119007933asd', 'Ошибка, неверно введен номер карты'),
                                                   ('SvfBNiok', 'Ошибка, неверно введен номер карты'),
                                                   ('', 'Ошибка, неверно введен номер карты')])

def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [(73654108430135874305, '**4305'),
                                                      (4530639492982, 'Ошибка, неверно введен номер счета'),
                                                      ('73654108430135874asd', 'Ошибка, неверно введен номер счета'),
                                                      ('SvfBNiokChIUa', 'Ошибка, неверно введен номер счета'),
                                                      ('', 'Ошибка, неверно введен номер счета')])

def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected