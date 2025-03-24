import unittest
from unittest.mock import patch

from src.utils import get_transactions


class TestJsonReader(unittest.TestCase):
    @patch("builtins.open")
    @patch("json.load")
    def test_read_json(self: "TestJsonReader", mock_json_load, mock_open):
        # Задаю тестовые данные
        mock_json_load.return_value = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        ]

        # Вызываю функцию и проверяю результат
        result = get_transactions("path/to/file.json")
        self.assertEqual(
            result,
            [
                {
                    "amount": "31957.58",
                    "currency_code": "RUB",
                    "currency_name": "руб.",
                    "date": "2019-08-26T10:50:58.294041",
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "id": 441945886,
                    "state": "EXECUTED",
                    "to": "Счет 64686473678894779589",
                }
            ],
        )
        mock_json_load.return_value = []

        # Вызываю функцию и проверяю результат
        result = get_transactions("path/to/file.json")
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open):
        # Вызываю свою функцию и проверяю, что она возвращает пустой список
        result = get_transactions("path/to/nonexistent/file.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
