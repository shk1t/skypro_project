from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования результатов выполнения функции.
    При успешном вызове функции записывает сообщение <имя_функции> ok.
    В случае исключения — логирует тип ошибки и переданные аргументы, затем повторно выбрасывает исключение.
    Если указан путь к файлу filename, лог записывается в файл (в режиме append).
    Иначе сообщение выводится в консоль
    """

    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                _write_log(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                _write_log(message)
                raise

        def _write_log(message: str) -> None:
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(message + "\n")
            else:
                print(message)

        return wrapper

    return inner
