import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.file_read import func_read_file_csv, func_read_file_excel


class TestReadCSVFile(unittest.TestCase):
    def test_valid_data(self):
        mock_data = ("id;state;date;amount;currency_name;currency_code;from;to;description\n1;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации")
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = func_read_file_csv("transactions.csv")
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["id"], "1")

    def test_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = func_read_file_csv("transactions.csv")
            self.assertEqual(result, [])

    def test_empty_file(self):
        with patch("builtins.open", mock_open(read_data="")):
            result = func_read_file_csv("transactions.csv")
            self.assertEqual(result, [])


class TestReadExcelFile(unittest.TestCase):
    def test_valid_data(self):
        mock_data = pd.DataFrame(
            {
                "id": [1],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": [16210],
                "currency_name": ["Sol"],
                "currency_code": ["PEN"],
                "from": ["Счет 58803664561298323391"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            }
        )
        with patch("pandas.read_excel", return_value=mock_data):
            result = func_read_file_excel("transactions_excel.xlsx")
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["id"], 1)

    def test_file_not_found(self):
        with patch("pandas.read_excel", side_effect=FileNotFoundError):
            result = func_read_file_excel("transactions_excel.xlsx")
            self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
