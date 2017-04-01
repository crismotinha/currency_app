from flask import Flask, render_template, request
from currency import routes, classes, helpers
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def return_graphic():
    selected_name = request.form["currency"].split("/")[0]
    selected_abbreviation = request.form["currency"].split("/")[1]
    selected_currency = classes.Currency(selected_name, selected_abbreviation)
   
    selected_currency = routes.get_quote(selected_currency)


    dates = helpers.get_last_week(datetime.today())
    
    return render_template('index.html', 
        dates = dates, currency = selected_currency)

@app.route('/', methods=['GET'])
def return_default():
    selected_currency = classes.Currency("Real", "BRL")
    selected_currency = routes.get_quote(selected_currency)


    dates = helpers.get_last_week(datetime.today())
    
    return render_template('index.html', 
        dates = dates, currency = selected_currency)

if __name__ == "__main__":
    app.run()