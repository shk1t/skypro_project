import masks as ms

def mask_account_card(card_info: str) -> str:
    """Функция, которая возвращает маску номера карты вместе с названием"""

    number_card = card_info[card_info.index(next(i for i in card_info if i.isdigit())):]

    return (
        card_info.replace(number_card, ms.get_mask_account(int(number_card)))
        if card_info[:4].lower() == "счет"
        else card_info.replace(number_card, ms.get_mask_card_number(int(number_card)))
    )


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ"""

    return date[8:10] + "." + date[5:7] + "." + date[:4]


print(mask_account_card("Maestro 7000792289606361"), mask_account_card("Счет 73654108430135874305"))