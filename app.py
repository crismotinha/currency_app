from flask import Flask, render_template, request
from currency import routes, classes, helpers
from datetime import datetime
import os

app = Flask(__name__)

def get_right_template(currency, dates):
    if None in currency.last_values:
        return render_template('error.html')
    else:
        return render_template('graphic.html', dates = dates, currency = currency)


@app.route('/', methods=['POST'])
def return_graphic():
    selected_name = request.form["currency"].split("/")[0]
    selected_abbreviation = request.form["currency"].split("/")[1]
    selected_currency = classes.Currency(selected_name, selected_abbreviation)
    selected_currency = routes.get_quote(selected_currency)

    dates = helpers.get_last_week(datetime.today()) #pega a data dos últimos 7 dias

    return get_right_template(selected_currency, dates)
    

@app.route('/', methods=['GET'])
def return_default():
    selected_currency = classes.Currency("Real", "BRL")
    selected_currency = routes.get_quote(selected_currency)
    
    dates = helpers.get_last_week(datetime.today())
    
    return get_right_template(selected_currency, dates)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
