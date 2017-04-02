from currency import helpers
from datetime import date


def test_get_last_week():
    today = date(2017, 4, 1)
    expected = ['2017-03-31', '2017-03-30', '2017-03-29',
    '2017-03-28', '2017-03-27', '2017-03-26', '2017-03-25']
    assert helpers.get_last_week(today) == expected

