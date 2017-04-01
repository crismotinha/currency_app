from flask import Flask, render_template
from currency import routes, classes
app = Flask(__name__)

@app.route('/')
def hello_world():
    coin = classes.Currency("teste", "AMD")
    coin = routes.get_quote(coin)
    quotation = coin.last_values
    return render_template('index.html', name = coin.name , quotes=quotation)

if __name__ == "__main__":
    app.run()