import os
import tempfile

from src.decorators import log


def test_summ_function_from_file():
    # Тестирование с временным файлом
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name

    try:
        # Применяем декоратор с временным файлом
        @log(filename=filename)
        def my_function(x, y):
            return x + y

        # Вызываем функцию
        my_function(1, 2)
        my_function()

        # Проверяем содержимое временного файла
        with open(filename, "r") as file:
            logs = file.read()
            assert "my_function ok: 3" in logs
            assert "my_function error: TypeError. Inputs: (), {}" in logs

    finally:
        # Удаляем временный файл
        os.remove(filename)


def test_devision_function_from_file():
    # Тестирование с временным файлом
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name

    try:
        # Применяем декоратор с временным файлом
        @log(filename=filename)
        def my_function(x, y):
            return x / y

        # Вызываем функцию
        my_function(9, 3)
        my_function(2, 0)

        # Проверяем содержимое временного файла
        with open(filename, "r") as file:
            logs = file.read()
            assert "my_function ok: 3" in logs
            assert "my_function error: ZeroDivisionError. Inputs: (2, 0), {}" in logs
    finally:
        # Удаляем временный файл
        os.remove(filename)


def test_my_function(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 6)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok: 7\n"


def test_my_function_error(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function("1", 6)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: ('1', 6), {}\n"


def test_my_function_empty(capsys):
    @log(filename="")
    def my_function(x, y):
        return x / y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError. Inputs: (2, 0), {}\n"
