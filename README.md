# учебный проект
# цель проекта
разработка фичи, которая показывает несколько последних успешных банковских операций клиента.
# инструкция по установке
1. клонирование репозитория 
```
git clone git@github.com:shk1t/skypro_project.git
```
2. проверка poetry
```
poetry --version
```
3. установка зависимостей проекта
```
poetry install
```
4. активация окружения
```
poetry shell
```
# модули проекта
# main.py
## основной модуль проекта, в котором вызываются функции
### далее под каждый модуль будут примеры вызова их фукнций в модуле main.py
# masks.py
## модуль содержит в себе две функции:
### 1. get_mask_card_number (маскирует номер карты)
### 2. get_mask_account (маскирует номер счета)
# аргументы функций
## 1. **get_mask_card_number**
- `card_number` - номер карты

**возвращает:**
замаскированный номер карты
## 2. **get_mask_account**
- `account_number` - номер счета

**возвращает:**
замаскированный номер счета
## пример вызова в модуле main.py
```
import masks as ms


def main() -> None:
    """Выводит результат работы функций get_mask_card_number и get_mask_account из модуля masks.py"""

    print(ms.get_mask_card_number(7000792289606361), ms.get_mask_account(73654108430135874305), sep="\n")


if __name__ == "__main__":
    main()
```
# widget.py
## модуль содержит в себе две функции:
### 1. mask_account_card (возвращает маску номера карты вместе с названием)
### 2. get_date (возвращает дату в формате "ДД.ММ.ГГГГ")
# аргументы функций
## 1. **mask_account_card**
- `card_info` - строка с информацией о карте

**возвращает:**
строку с маской номера карты вместе с названием
## 2. **get_date**
- `date` - дата в формате "2024-03-11T02:26:18.671407"

**возвращает:**
строку с датой в формате "ДД.ММ.ГГГГ"
# пример вызова в модуле main.py
```
import widget as wg


def main() -> None:
    """Выводит результат работы функций get_mask_card_number и get_mask_account из модуля masks.py"""

    print(wg.mask_account_card("Maestro 1596837868705199"), wg.get_date("2024-03-11T02:26:18.671407"), sep="\n")


if __name__ == "__main__":
    main()
```
# processing.py
## модуль содержит в себе две функции:
### 1. filter_by_state (фильтрует список словарей по state)
### 2. sort_by_date (сортирует список словарей по дате)
# аргументы функций
## 1. **filter_by_state**
- `data` - список словарей
- `state` - по умолчанию "EXECUTED"

**возвращает:**
отсортированный список словарей по state
## 2. **sort_by_date**
- `data` - список словарей
- `sort_order` - тип сортировки, по умолчанию True (убывание)


**возвращает:**
отсортированный список словарей по дате
## пример вызова в модуле main.py
```
import processing as pr


data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def main() -> None:
    """Выводит результат работы функций filet_by_state и sort_by_date из модуля processing.py"""

    print(pr.filter_by_state(data), pr.sort_by_date(data))


if __name__ == "__main__":
    main()
```
# generators.py
## модуль содержит в себе три функции:
### 1. filter_by_currency (генератор, выводящий транзакции, которые соответствуют коду)
### 2. transaction_descriptions (генератор, который выводит описание каждой транзакции)
### 3. card_number_generator (генератор, который выводит XXXX XXXX XXXX XXXX в заданном диапазоне)
# аргументы функций
## 1. **filter_by_currency**
- `transactions` - список транзакций (словарей)
- `currency_code` - код валюты

**возвращает:**
поочередно выдает транзакции, где code соответствует заданному currency_code
## 2. **transaction_descriptions**
- `transactions` - список транзакций (словарей)

**возвращает:**
возвращает описание каждой операции по очереди
## 3. **card_number_generator**
- `start` - начало диапазона X (0<X<Y)
- `end` - конец диапазона Y (X<Y<=9999999999999999)

**возвращает:**
выдает номера банковских карт в формате XXXX XXXX XXXX XXXX

# тестирование
## структура тестов:
 • `test_masks.py`

**проверяет корректность работы функций get_mask_card_number(), get_mask_account() из модуля masks.py:**

 • `test_widget.py`

**тестирует функции mask_account_card(), get_date() из модуля widget.py:**

 • `test_processing.py`

**проверяет фильтрацию операций по статусу filter_by_state() из модуля processing.py:**

 • `test_generators.py`

 **проверяет все функции из модуля generators.py**

# для запуска всех тестов из корня проекта используйте команду:
`
pytest
`