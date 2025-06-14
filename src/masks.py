def get_mask_card_number(card_number: int) -> str:
    """Функция, которая возвращает маску номера карты"""

    first_part = str(card_number)[:6]
    last_part = str(card_number)[-4:]

    return (
        f"{first_part[:4]} {first_part[4:]}** **** {last_part}"
        if len(str(card_number)) == 16 and isinstance(card_number, int)
        else "Некорректные данные"
    )


def get_mask_account(account_number: int) -> str:
    """Функция, которая возвращает маску номера счета"""

    return (
        "**" + str(account_number)[-4:]
        if len(str(account_number)) == 20 and isinstance(account_number, int)
        else "Некорректные данные"
    )
