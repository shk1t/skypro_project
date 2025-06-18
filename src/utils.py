import json
import pandas as pd
from logger_config import setup_logger
from typing import Optional

logger = setup_logger("utils.py", "logs/utils.log")


def load_transactions_json(filename: str) -> list[Optional[dict]]:
    """
    Загружает список транзакций из JSON-файла.
    """
    logger.info("Работа с JSON-файлом")
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


def load_transactions_csv(filename: str) -> list[Optional[dict]]:
    """
    Загружает список транзакций из CSV-файла.
    """
    logger.info("Работа с JSON-файлом")
    try:
        csv_data = pd.read_csv("data/transactions.csv", sep=";")
        logger.info("Файл успешно прочитан")
        return csv_data.to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def load_transactions_excel(filename: str) -> list[Optional[dict]]:
    """
    Загружает список транзакций из EXCEL-файла.
    """
    logger.info("Работа с JSON-файлом")
    try:
        excel_data = pd.read_excel("data/transactions_excel.xlsx")
        logger.info("Файл успешно прочитан")
        return excel_data.to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка: {e}")
