import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    encoding="UTF-8",
    filemode="w",
)
logger = logging.getLogger("masks")


def get_mask_card_number(card_number: int | str) -> str:
    """Возвращает маску номера карты: видны первые 6 и последние 4 цифры номера"""
    if len(str(card_number)) == 16:
        mask_card_number = str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[12:]
        logger.info("Маска номера карты успешно сформирована")
        return mask_card_number
    logger.error("Ошибка, количество цифр в номере карты не равно 16")
    return "Ошибка, неверно введен номер карты"


# print(get_mask_card_number('0329774489991288'))


def get_mask_account(account_number: int | str) -> str:
    """Возвращает маску номера счета в виде ** и последних 4-х цифр счета"""
    if len(str(account_number)) == 20:
        mask_account_number = "**" + str(account_number)[len(str(account_number)) - 4:]
        logger.info("Маска номера счета успешно сформирована")
        return mask_account_number
    logger.error("Ошибка, количество цифр в номере счета не равно 20")
    return "Ошибка, неверно введен номер счета"

# print(get_mask_card_number(""))
# print(get_mask_account(''))
