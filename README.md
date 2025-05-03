# учебный проект
# processing.py
модуль содержит в себе две функции:
1. filter_by_state (фильтрует список словарей по state)
2. sort_by_date (сортирует список словарей по дате)
# описание функций
## filter_by_state
фильтрует список словарей, оставляя только те, которые соответсвуют аргументу state

**аргументы:**
- `data` - список словарей
- `state` - по умолчанию "EXECUTED"

**возвращает:**
отсортированный список по state

## sort_by_date
сортирует список словарей по дате

**аргументы:**
- `data` - список словарей
- `sort_order` - тип сортировки, по умолчанию "убывание"

## пример вызова в модуле main.py
```python
from processing import filter_by_state, sort_by_date

data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def main() -> None:
    """Выводит результат работы функций filet_by_state и sort_by_date из модуля processing.py"""

    print(filter_by_state(data))
    print(sort_by_date(data))


if __name__ == "__main__":
    main()
