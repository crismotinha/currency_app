from flask import Flask, render_template, request
from currency import routes, classes, helpers
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def return_graphic():
    #cria uma instância de Currency com as informações do request feito pelo botão
    selected_name = request.form["currency"].split("/")[0]
    selected_abbreviation = request.form["currency"].split("/")[1]
    selected_currency = classes.Currency(selected_name, selected_abbreviation)
    selected_currency = routes.get_quote(selected_currency)

    dates = helpers.get_last_week(datetime.today()) #pega a data dos últimos 7 dias

    if None in selected_currency.last_values:
        return render_template('error.html')
    else:
        return render_template('graphic.html', dates = dates, currency = selected_currency)

@app.route('/', methods=['GET'])
def return_default():
     #cria uma instância de Currency default, para exibição no primeiro carregamento da página
    selected_currency = classes.Currency("Real", "BRL")
    selected_currency = routes.get_quote(selected_currency)
    
    dates = helpers.get_last_week(datetime.today())
    
    if None in selected_currency.last_values:
        return render_template('error.html')
    else:
        return render_template('graphic.html', dates = dates, currency = selected_currency)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
