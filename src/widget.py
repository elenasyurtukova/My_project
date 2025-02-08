from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(model_number: str) -> str:
    """Функция, которая маскирует тип и номер карты или счета"""
    if 'Счет' in model_number:
        mask_model_number = 'Счет ' + get_mask_account(int(model_number[5:]))
    else:
        mask_model_number = model_number[:-16] + get_mask_card_number(int(model_number[-16:]))
    return mask_model_number


def get_date(date: str) -> str:
    """Функция, которая меняет формат даты"""
    formated_date = date[8:10]+'.'+date[5:7]+'.'+date[:4]
    return formated_date
