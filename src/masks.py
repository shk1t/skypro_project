def get_mask_card_number(card_number: int) -> str:
    """Функция, которая возвращает маску номера карты"""
    first_part = str(card_number)[:6]
    last_part = str(card_number)[-4:]

    return f"{first_part[:4]} {first_part[4:]}** **** {last_part}"


def get_mask_account(account_number: int) -> str:
    """Функция, которая возвращает маску номера счета"""

    return "**" + str(account_number)[-4:]
