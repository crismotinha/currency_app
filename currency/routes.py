import os
from datetime import datetime
import requests
from currency import helpers


currency_api_key = os.environ.get('CURRENCY_API_KEY')

req_params = {'access_key': currency_api_key, 'format': 1}

url = 'http://www.apilayer.net/api/historical'

def get_quote(currency):
    req_params["currencies"] = currency.abb
    week = helpers.get_last_week(datetime.today())
    for day in week:
        req_params["date"] = day
        r = requests.get(url, params = req_params)
        if r.json()["success"]:
            currency.add_value(r.json()["quotes"]["USD"+currency.abb])
        else:
            currency.add_value(None)
    return currency
