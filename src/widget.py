from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(model_number: str) -> Any:
    """Функция, которая маскирует тип и номер карты или счета"""
    if not isinstance(model_number, str):
        raise TypeError("Ошибка типа данных")

    if "Счет" in model_number:
        if len(model_number[5:]) == 20 and model_number[5:].isdigit():
            mask_model_number = "Счет " + get_mask_account(model_number[5:])
            return mask_model_number
        else:
            return "Ошибка, некорректно указаны данные"
    else:
        if model_number[-16:].isdigit() and model_number[:-16].replace(" ", "").isalpha():
            mask_model_number = model_number[:-16] + get_mask_card_number(model_number[-16:])
            return mask_model_number
        else:
            return "Ошибка, некорректно указаны данные"


def get_date(date: str) -> str:
    """Функция, которая меняет формат даты"""
    formated_date = date[8:10] + "." + date[5:7] + "." + date[:4]
    return formated_date

# print(mask_account_card('Discover 0329774489991288'))