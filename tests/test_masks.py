import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected_mask",
    [
        (1234567890123456, "1234 56** **** 3456"),
        (111122223333444478, "Некорректные данные"),
        ([], "Некорректные данные"),
        ("4000000000000000", "Некорректные данные"),
    ],
)
def test_get_mask_card_number(card_number, expected_mask):
    assert get_mask_card_number(card_number) == expected_mask


@pytest.mark.parametrize(
    "account_number, expected_mask",
    [(12345678901234567890, "**7890"), ("111122223333", "Некорректные данные"), (55556666777788889999, "**9999"), ({}, "Некорректные данные")]
)
def test_get_mask_account(account_number, expected_mask):
    assert get_mask_account(account_number) == expected_mask
