import src.masks as ms


def mask_account_card(card_info: str) -> str:
    """Функция, которая возвращает маску номера карты вместе с названием"""

    number_card = (
        card_info[card_info.index(next(i for i in card_info if i.isdigit())) :] if type(card_info) == str else ""
    )

    if number_card.isdigit():
        mask_number_card = (
            ms.get_mask_account(int(number_card))
            if card_info[:4].lower() == "счет"
            else ms.get_mask_card_number(int(number_card))
        )

        return card_info.replace(number_card, mask_number_card)
    return "Некорректные данные"


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ"""

    return date[8:10] + "." + date[5:7] + "." + date[:4] if isinstance(date, str) and len(date) == 26 else "Некорректные данные"
