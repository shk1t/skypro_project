import masks as ms
from datetime import datetime as dt
from logger_config import setup_logger

logger = setup_logger("widget.py", "logs/widget.log")

def mask_account_card(card_info: str) -> str:
    """
    Функция, которая возвращает маску номера карты или счета вместе с названием.
    """
    if not card_info:
        logger.info(f"Счет не указан")
        return "Нет данных"
    if not isinstance(card_info, str):
        logger.warning(f"Данные неккоректны: {card_info}")
        return "Некорректные данные"
    # Поиск первой цифры
    try:
        logger.info(f"Поиск первой цифры")
        first_digit_index = next(i for i, c in enumerate(card_info) if c.isdigit())
    except StopIteration:
        logger.warning(f"Нет цифр в строке: {card_info}")
        return "Некорректные данные"  # Нет цифр в строке

    number_card = card_info[first_digit_index:]

    if not number_card.isdigit():
        logger.warning("Неверный формат данных карты/счета")
        return "Некорректные данные"

    try:
        if card_info[:first_digit_index].strip().lower() == "счет":
            masked_number = ms.get_mask_account(number_card)
            logger.info(f"Маска счета: {masked_number}")
        else:
            masked_number = ms.get_mask_card_number(number_card)
            logger.info(f"Маска номера карты: {masked_number}")
    except Exception:
        logger.warning("Некорректные данные")
        return "Некорректные данные"  # например, слишком короткое число или ошибка в `ms`

    return card_info.replace(number_card, masked_number)


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ"""

    return (
        dt.fromisoformat(date)
    )
