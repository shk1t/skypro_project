import pytest
from src.decorators import log

@log()
def double(x):
    return x * 2

@log()
def fail():
    raise ValueError("test error")

def test_success_log_to_console(capsys):
    double(2)
    captured = capsys.readouterr()
    assert "double ok" in captured.out

def test_error_log_to_console(capsys):
    with pytest.raises(ValueError):
        fail()

    captured = capsys.readouterr()
    assert "fail error: ValueError. Inputs: (), {}" in captured.out