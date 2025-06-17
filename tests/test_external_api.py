from unittest.mock import patch, Mock
from src.external_api import convert_amount_to_rub


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"result": 95.5}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": 1.0,
            "currency": {
                "code": "USD"
            }
        }
    }

    result = convert_amount_to_rub(transaction)
    assert result == 95.5
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_eur_to_rub(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"result": 102.3}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": 1.0,
            "currency": {
                "code": "EUR"
            }
        }
    }

    result = convert_amount_to_rub(transaction)
    assert result == 102.3
    mock_get.assert_called_once()


def test_convert_rub_does_not_call_api():
    transaction = {
        "operationAmount": {
            "amount": 500.0,
            "currency": {
                "code": "RUB"
            }
        }
    }

    result = convert_amount_to_rub(transaction)
    assert result == 500.0
