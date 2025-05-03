def filter_by_state(data: list[dict], state: str="EXECUTED") -> list:
    """Функция, которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    return [i for i in data if i["state"] == state]
