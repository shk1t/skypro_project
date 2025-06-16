import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_info, expected_mask",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 73654108430135874305Счет 73654108430135874305", "Некорректные данные"),
        ([1, 2, 3, 4], "Некорректные данные"),
    ],
)
def test_mask_account_card(card_info, expected_mask):
    assert mask_account_card(card_info) == expected_mask


@pytest.mark.parametrize(
    "date, expected_mask",
    [
        ([1, 2, 3, 4], "Некорректные данные"),
        ("12345", "Некорректные данные"),
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        (54321, "Некорректные данные"),
    ],
)
def test_get_date(date, expected_mask):
    assert get_date(date) == expected_mask
