def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты: видны первые 6 и последние 4 цифры номера"""
    if len(str(card_number)) == 16:
        if str(card_number).isdigit():
            mask_card_number = str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[12:]
            return mask_card_number
        return "Ошибка, неверно введен номер карты"
    return "Ошибка, неверно введен номер карты"


def get_mask_account(account_number: int) -> str:
    """Возвращает маску номера счета в виде ** и последних 4-х цифр счета"""
    if len(str(account_number)) == 20:
        if str(account_number).isdigit():
            mask_account_number = "**" + str(account_number)[len(str(account_number)) - 4:]
            return mask_account_number
        return "Ошибка, неверно введен номер счета"
    return "Ошибка, неверно введен номер счета"


# print(get_mask_card_number(""))
# print(get_mask_account(''))
