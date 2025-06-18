from logger_config import setup_logger


logger = setup_logger("masks.py", "logs/masks.log")


def get_mask_card_number(card_number: int) -> str:
    """Функция, которая возвращает маску номера карты"""
    try:
        first_part = str(card_number)[:6]
        last_part = str(card_number)[-4:]

        if len(str(card_number)) == 16 and isinstance(card_number, int):
            masked = f"{first_part[:4]} {first_part[4:]}** **** {last_part}"
            logger.info(f"Маска карты успешно создана: {masked}")
            return masked
        else:
            logger.warning(f"Некорректные данные карты: {card_number}")
            return "Некорректные данные"
    except Exception as e:
        logger.error(f"Ошибка в get_mask_card_number: {e}")
        return "Ошибка при обработке"


def get_mask_account(account_number: int) -> str:
    """Функция, которая возвращает маску номера счета"""
    try:
        if len(str(account_number)) == 20 and isinstance(account_number, int):
            masked = "**" + str(account_number)[-4:]
            logger.info(f"Маска счёта успешно создана: {masked}")
            return masked
        else:
            logger.warning(f"Некорректные данные счёта: {account_number}")
            return "Некорректные данные"
    except Exception as e:
        logger.error(f"Ошибка в get_mask_account: {e}")
        return "Ошибка при обработке"

get_mask_card_number(7000792289606361)
get_mask_account(73654108430135874305)