def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты: видны первые 6 и последние 4 цифры номера"""
    mask_card_number = str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[12:]
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Возвращает маску номера счета в виде ** и последних 4-х цифр счета"""
    mask_account_number = "**" + str(account_number)[len(str(account_number)) - 4:]
    return mask_account_number


# print(get_mask_card_number(7000792289606361))
# print(get_mask_account(73654108430135874305))
