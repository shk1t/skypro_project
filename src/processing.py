import re
from collections import Counter


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция, которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """

    if not isinstance(data, list):
        return []
    return [i for i in data if isinstance(i, dict) and i.get("state") == state]


def sort_by_date(data: list[dict], sort_order: bool = True) -> list[dict]:
    """Функция, которая сортирует список по дате"""

    return sorted(data, key=lambda x: x["date"], reverse=sort_order)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Ищет операции, в которых в поле 'description' содержится слово, заданное параметром search.
    Использует регулярные выражения. Поиск нечувствителен к регистру.
    """

    pattern = re.compile(rf"{search}", re.IGNORECASE)

    return [item for item in data if isinstance(item.get("description"), str) and pattern.search(item["description"])]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Возвращает словарь {категория: количество} по списку категорий, найденных в описании.
    """
    counted_descriptions = Counter(
        [i["description"] for i in data if i["description"].lower() in list(map(lambda x: x.lower(), categories))]
    )

    return counted_descriptions
