from flask import Flask
import os
import requests
from classes import Currency
import helpers

app = Flask(__name__)

currency_api_key = os.environ.get('CURRENCY_API_KEY')

req_params = {'access_key': currency_api_key, 'format': 1}

url = 'http://www.apilayer.net/api/historical'

def get_quote(currency):
    req_params["currencies"] = currency.abb
    week = helpers.get_last_week()
    for day in week:
        req_params["date"] = day
        r = requests.get(url, params = req_params)
        currency.add_value(r.json()["quotes"]["USD"+currency.abb])
    return currency


if __name__ == "__main__":
    coin = Currency("teste", "AMD")
    get_quote(coin)

