from unittest.mock import Mock, patch

import pytest

from src.external_api import get_amount_in_rub


def test_get_amount_in_rub_from_usd():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_transaction = {
        "id": 854048120,
        "state": "EXECUTED",
        "date": "2019-03-29T10:57:20.635567",
        "operationAmount": {"amount": "30234.99", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на счет",
        "from": "Visa Classic 1203921041964079",
        "to": "Счет 34616199494072692721",
    }
    mock_response.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 30234.99},
        "info": {"timestamp": 1742108711, "rate": 85.504654},
        "date": "2025-03-16",
        "result": 2585232.358643,
    }

    with patch("requests.get", return_value=mock_response):
        result = get_amount_in_rub(mock_transaction)
        assert result == 2585232.36


def test_get_amount_in_rub_no_code_currency():
    mock_response = Mock()
    mock_response.status_code = 400
    mock_transaction = {
        "id": 854048120,
        "state": "EXECUTED",
        "date": "2019-03-29T10:57:20.635567",
        "operationAmount": {"amount": "30234.99", "currency": {"name": "USD", "code": ""}},
        "description": "Перевод с карты на счет",
        "from": "Visa Classic 1203921041964079",
        "to": "Счет 34616199494072692721",
    }

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Failed to get currency rate"):
            get_amount_in_rub(mock_transaction)
