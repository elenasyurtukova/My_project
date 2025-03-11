from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, логирует работу функции и ее результат в файл или в консоль"""

    def wrapped(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
                log_mess = f"{function.__name__} ok: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{log_mess}\n")
                else:
                    print(log_mess)
            except Exception as e:
                result = None
                log_mess = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{log_mess}\n")
                else:
                    print(log_mess)
                raise Exception(f"Ошибка: {type(e).__name__}")
            return result

        return inner

    return wrapped


# @log(filename="mylog.txt")
# @log()
# def my_function(x: int | float, y: int | float) -> int | float:
#     """функция, делит 2 числа"""
#     return x + y
#
# my_function("1",6)
# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:
# my_function ok
# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.
