import logging


def setup_logger(name: str, filename: str, level: int = logging.INFO) -> logging.Logger:
    """Создает и возвращает логгер, который записывает в файл"""

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        file_handler = logging.FileHandler(filename, mode="w", encoding="utf-8")
        file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger
