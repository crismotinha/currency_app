from currency import classes, helpers
from unittest.mock import MagicMock, Mock, patch
import sys


def test_get_quote():
    fake_json = {
        "quotes": {
            "USDBRL": "1"
            }
        }
    fake_response = Mock()
    fake_response.json = MagicMock(return_value=fake_json)
    sys.modules['requests'] = Mock()
    sys.modules['requests'].get = MagicMock(return_value=fake_response)

    currency = classes.Currency("Real", "BRL")
    
    from currency import routes
    routes.get_quote(currency)

    assert currency.last_values == ['1','1','1','1','1','1','1']



