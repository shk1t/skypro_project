def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    return [i for i in data if i["state"] == state]


def sort_by_date(data: list[dict], sort_order: str = "убывание") -> list[dict]:
    """Функция, которая сортирует список по дате"""
    if sort_order == "убывание":
        return sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted(data, key=lambda x: x["date"])
