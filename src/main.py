from utils import load_transactions_json, load_transactions_csv, load_transactions_xlsx
from processing import filter_by_state, sort_by_date, process_bank_search
from generators import filter_by_currency
from widget import get_date, mask_account_card
from logger_config import setup_logger

logger = setup_logger("main.py", "logs/main.log")


def main() -> None:
    """
    Основная функция программы обработки банковских транзакций.
    
    - Запрашивает у пользователя тип файла (JSON, CSV, XLSX);
    - Загружает транзакции из выбранного файла;
    - Запрашивает статус транзакций для фильтрации (EXECUTED, CANCELED, PENDING);
    - Запрашивает необходимость сортировки по дате;
    - Запрашивает фильтрацию только по рублевым операциям;
    - Запрашивает поиск по ключевому слову в описании;
    - Выводит отфильтрованные транзакции или сообщение об отсутствии подходящих;
    - Логирует действия пользователя.
    """

    

    while True:
        file_selection = int(input("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n\n"))
        if file_selection == 1:
            data = load_transactions_json("data/transactions.json")
            print("\nДля обработки выбран JSON-файл.\n")
            logger.info("Загружен JSON-файл")
        elif file_selection == 2:
            data = load_transactions_csv("data/transactions.csv")
            print("\nДля обработки выбран CSV-файл.\n")
            logger.info("Загружен CSV-файл")
        elif file_selection == 3:
            data = load_transactions_xlsx("data/transactions.xlsx")
            print("\nДля обработки выбран XLSX-файл.\n")
            logger.info("Загружен XLSX-файл")
        else:
            print("Нужно ввести только число от 1 до 3")
            logger.warning("Неверный выбор файла")
            continue

        break

    # Фильтрация по статусу
    while True:
        status_selection = input("Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\n").upper()
        if status_selection in {"EXECUTED", "CANCELED", "PENDING"}:
            data = filter_by_state(data, state=status_selection)
            print(f'\nОперации отфильтрованы по статусу "{status_selection}"')
            logger.info(f'Фильтрация по статусу: {status_selection}')
            break
        else:
            print(f'\nСтатус операции "{status_selection}" недоступен.')

    # Сортировка по дате
    if input("Отсортировать операции по дате? Да/Нет\n").strip().lower() == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        reverse = order != "по возрастанию"
        data = sort_by_date(data, sort_order=reverse)
        logger.info(f"Сортировка по дате: {'по убыванию' if reverse else 'по возрастанию'}")

    # Фильтрация по рублям
    if input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower() == "да":
        data = list(filter_by_currency(data, "RUB"))
        logger.info("Фильтрация только рублевых транзакций")

    # Поиск по ключевому слову
    if input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower() == "да":
        keyword = input("Введите ключевое слово для поиска в описании: ").strip()
        data = process_bank_search(data, keyword)
        logger.info(f"Поиск по ключевому слову: {keyword}")

    print("\nРаспечатываю итоговый список транзакций...\n")

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        logger.info("Итоговая выборка пуста")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}\n")
        flag = True if data[0].get("operationAmount") else False
        for item in data:
            date = get_date(item.get("date", ""))
            desc = item.get("description", "Нет описания")
            from_ = mask_account_card(item.get("from", ""))
            to = mask_account_card(item.get("to", ""))
            if flag:
                amount = item["operationAmount"]["amount"]
                currency = item["operationAmount"]["currency"]["code"]
            else:
                amount = item["amount"]
                currency = item["currency_code"]

            print(f"{date} {desc}")
            if from_ and to:
                print(f"{from_} -> {to}")
            elif to:
                print(f"{to}")
            print(f"Сумма: {amount} {currency}\n")

        logger.info(f"Выведено {len(data)} транзакций")

if __name__ == "__main__":
    main()
