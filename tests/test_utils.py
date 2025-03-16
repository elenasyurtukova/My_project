import unittest
from unittest.mock import patch

from src.utils import get_transactions


class TestJsonReader(unittest.TestCase):
    @patch('builtins.open')
    @patch('json.load')
    def test_read_json(self: "TestJsonReader", mock_json_load, mock_open):
        # Задай тестовые данные
        mock_json_load.return_value = [{
  "id": 441945886,
  "state": "EXECUTED",
  "date": "2019-08-26T10:50:58.294041",
  "operationAmount": {
    "amount": "31957.58",
    "currency": {
      "name": "руб.",
      "code": "RUB"
    }
  },
  "description": "Перевод организации",
  "from": "Maestro 1596837868705199",
  "to": "Счет 64686473678894779589"
}]

        # Вызови свою функцию и проверь результат
        result = get_transactions('path/to/file.json')
        self.assertEqual(result, [{
  "id": 441945886,
  "state": "EXECUTED",
  "date": "2019-08-26T10:50:58.294041",
  "operationAmount": {
    "amount": "31957.58",
    "currency": {
      "name": "руб.",
      "code": "RUB"
    }
  },
  "description": "Перевод организации",
  "from": "Maestro 1596837868705199",
  "to": "Счет 64686473678894779589"
}])
        mock_json_load.return_value = []

        # Вызови свою функцию и проверь результат
        result = get_transactions('path/to/file.json')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()