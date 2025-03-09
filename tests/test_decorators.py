from src.decorators import log


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
        return x + y

    my_function()
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (), {}\n"
