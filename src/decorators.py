from typing import Callable, Optional, Any
from functools import wraps


def log(filename: Optional[str] = None) -> Callable:
    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
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
