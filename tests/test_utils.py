import os
import pytest
from src.utils import (
    load_transactions_json,
    load_transactions_csv,
    load_transactions_excel,
)

# Пути к тестовым файлам
DATA_DIR = "data"
JSON_FILE = os.path.join(DATA_DIR, "operations.json")
CSV_FILE = os.path.join(DATA_DIR, "transactions.csv")
EXCEL_FILE = os.path.join(DATA_DIR, "transactions_excel.xlsx")
BAD_FILE = os.path.join(DATA_DIR, "not_found.json")


def test_load_transactions_json():
    result = load_transactions_json(JSON_FILE)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)
    assert "amount" in result[0]


def test_load_transactions_csv():
    result = load_transactions_csv(CSV_FILE)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)
    assert "amount" in result[0]


def test_load_transactions_excel():
    result = load_transactions_excel(EXCEL_FILE)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)
    assert "amount" in result[0]


def test_load_transactions_json_file_not_found():
    result = load_transactions_json(BAD_FILE)
    assert result == []


def test_load_transactions_csv_file_not_found():
    result = load_transactions_csv(BAD_FILE)
    assert result == []


def test_load_transactions_excel_file_not_found():
    result = load_transactions_excel(BAD_FILE)
    assert result == []
