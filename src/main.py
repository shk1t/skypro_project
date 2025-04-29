import masks as ms


def main() -> None:
    """Выводит результат работы функций get_mask_card_number и get_mask_account из модуля masks.py"""

    print(ms.get_mask_card_number(7000792289606361), ms.get_mask_account(73654108430135874305))


if __name__ == "__main__":
    main()
