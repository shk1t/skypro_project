def mask_account_card(card_info: str) -> str:
    """Функция, которая возвращает маску номера карты вместе с названием"""

    for i in card_info:
        if i.isdigit():
            number_card = card_info[card_info.index(i):]
            break

    if card_info[:4].lower() == "счет":
        return card_info.replace(number_card, "**" + number_card[-4:])

    return card_info.replace(number_card, number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[-4:])


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ"""

    return date[8:10] + "." + date[5:7] + "." + date[:4]
