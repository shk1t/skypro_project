import pytest

from src.processing import filter_by_state  # Импортируй корректно по своему пути


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # 1. Обычные данные, часть 'EXECUTED', часть 'CANCELED'
        (
            [
                {"id": 1, "state": "EXECUTED"},
                {"id": 2, "state": "CANCELED"},
                {"id": 3, "state": "EXECUTED"},
            ],
            [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}],
        ),
        # 2. Все записи 'CANCELED'
        ([{"id": 1, "state": "CANCELED"}, {"id": 2, "state": "CANCELED"}], []),
        # 3. Пустой список
        ([], []),
        # 4. Словари без ключа 'state'
        ([{"id": 1}, {"id": 2, "status": "EXECUTED"}], []),
        # 5. Смешанные типы: словарь и строка
        ([{"id": 1, "state": "EXECUTED"}, "invalid", 123, None], [{"id": 1, "state": "EXECUTED"}]),
        # 6. Указание другого значения фильтра
        (
            [{"id": 1, "state": "DONE"}, {"id": 2, "state": "CANCELED"}],
            [],
        ),
        # Невалидные входные типы (ожидается ошибка)
        (None, []),
        (123, []),
        ("not a list", []),
        ({"state": "EXECUTED"}, []),
    ],
)
def test_filter_by_state(input_data, expected_output):
    assert filter_by_state(input_data) == expected_output
