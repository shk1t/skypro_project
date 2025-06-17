import pytest

from src.decorators import log


@log()
def fail():
    raise ValueError("test error")


def test_success_log_to_console(capsys):

    @log()
    def double(x):
        return x * 2
    double(2)
    captured = capsys.readouterr()
    assert "double ok" in captured.out


def test_error_log_to_console(capsys):

    @log()
    def fail():
        raise ValueError("test error")

    with pytest.raises(ValueError):
        fail()

    captured = capsys.readouterr()
    assert "fail error: ValueError. Inputs: (), {}" in captured.out


def test_log_success(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=log_file)
    def add(x, y):
        return x + y

    result = add(3, 4)
    assert result == 7

    content = log_file.read_text(encoding="utf-8")
    assert "add ok" in content


def test_log_error(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=log_file)
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    content = log_file.read_text(encoding="utf-8")
    assert "divide error: ZeroDivisionError" in content
    assert "Inputs: (1, 0), {}" in content


def test_log_multiple_calls(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=log_file)
    def double(x):
        return x * 2

    double(2)
    double(5)

    content = log_file.read_text(encoding="utf-8")
    assert content.count("double ok") == 2
