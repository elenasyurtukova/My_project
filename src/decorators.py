from functools import wraps
from typing import Any, Callable

def log(filename: str | None = None) -> Callable:
    def wrapped(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
                log_mess = f"{function.__name__} ok: {function(*args, **kwargs)}"
            except Exception as e:
                log_mess = f"{function.__name__} error: TypeError. Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{log_mess}\n")
            else:
                print(log_mess)
            return result
        return inner
    return wrapped

@log(filename="mylog.txt")
# @log()
def my_function(x, y):
    return x + y

my_function(3, 2)

# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:
# my_function ok
# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.
