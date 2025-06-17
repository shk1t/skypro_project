import tempfile
import os
from src.utils import load_transactions


def create_temp_file(content: str) -> str:
    """Создание временного файла с заданным содержимым"""
    temp = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    temp.write(content)
    temp.close()
    return temp.name


def test_load_valid_json_list():
    path = create_temp_file('[{"id": 1}, {"id": 2}]')
    result = load_transactions(path)
    assert isinstance(result, list)
    assert result == [{"id": 1}, {"id": 2}]
    os.remove(path)


def test_load_json_not_list():
    path = create_temp_file('{"id": 1}')
    result = load_transactions(path)
    assert result == []
    os.remove(path)


def test_load_empty_file():
    path = create_temp_file('')
    result = load_transactions(path)
    assert result == []
    os.remove(path)


def test_file_not_found():
    result = load_transactions('non_existent_file.json')
    assert result == []


def test_invalid_json():
    path = create_temp_file('{invalid json')
    result = load_transactions(path)
    assert result == []
    os.remove(path)
