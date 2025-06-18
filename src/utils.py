import json
from src.logger_config import setup_logger
from typing import Optional

logger = setup_logger("utils.py", "logs/utils.log")


def load_transactions(filename: str) -> list[Optional[dict]]:
    """
    Загружает список транзакций из JSON-файла.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из {filename}")
                return data
            logger.warning(f"Файл {filename} не содержит список.")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {filename}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {filename}")
        return []

load_transactions("data/operations.json")