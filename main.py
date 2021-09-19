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
    author = None
    quote_id = None
    #bar = request.args.to_dict()

    if 'id' in request.args:
        quote_id = int(request.args['id'])
        return jsonify(db.read_quotes_in_table(quote_id))

    else:
        if request.args.get('count'):
            count = int(request.args['count'])
        else:
            count = 1

        if request.args.get('author'):
            author = request.args['author']
        else:
            author = None

        if request.args.get('book_title'):
            book_title = request.args['book_title']
        else:
            book_title = None

        print(count)
        print(author)
        print(book_title)


    '''
    if 'id' in request.args:
        quote_id = int(request.args['id'])
    elif 'author' in request.args:
        author = request.args['author']
    else:
        return "error"
    if author:
        print(author)
    return jsonify(db.read_quotes_in_table(quote_id))
    '''
    return 'sacessful', 200

app.run()
