import random
import flask
from flask import request, jsonify

from db_admonistrate import DateBaseA

db = DateBaseA()

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def home():
    """Домашняя страница"""
    return "<h1>Hello World!<h1>"


@app.route('/api/random', methods=['GET'])
def return_a_random_quote():
    """Выдаёт случайную цитату из таблицы QuoBook"""
    return jsonify(db.read_quotes_in_table(random.randint(1, db.count_id())))


@app.route('/api/v1', methods=['GET'])
def returns_a_specific_quote():
    """Возвращает определённую цитату, которую задал пользователь"""
    if 'id' in request.args:
        quote_id = int(request.args['id'])
    else:
        return "error"

    return jsonify(db.read_quotes_in_table(quote_id))


app.run()
