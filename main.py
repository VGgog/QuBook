import random
import flask
from flask import request, jsonify

from db_admonistrate import DateBaseA
from Functions import give_a_nice_quote, return_list_result, return_sorted_quotes

db = DateBaseA()

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def home():
    """Домашняя страница"""
    return "<h1>Hello World!<h1>"


@app.route('/api', methods=['GET'])
def returns_a_specific_quote():
    """Возвращает определённую цитату, которую задал пользователь"""
    if request.args.get('count'):
        # Определяет количество цитат, которые нужны пользователю

        try:
            count = int(request.args['count'])
        except ValueError:
            return 'Error'
    else:
        count = 1

    if 'id' in request.args:
        # Возвращает цитату по id
        try:
            quote_id = int(request.args['id'])
        except ValueError:
            return 'Error'

        if quote_id <= db.count_id():
            return jsonify(give_a_nice_quote(db.read_quotes_in_table(quote_id))), 200
        else:
            return 'Error, quote not found', 404

    elif 'author' in request.args:
        # Возвращает отсортированные по автору цитаты
        author = request.args.get('author')
        return return_list_result(return_sorted_quotes(count, author, index=1))

    elif 'book_title' in request.args:
        # Возвращает отсортированные по названию книги цитаты
        book_title = request.args.get('book_title')
        return return_list_result(return_sorted_quotes(count, book_title, index=2))

    else:
        # Возвращает случайные цитаты(количество задаёт пользователь)
        quotes = []
        while len(quotes) < count:
            quotes.append(give_a_nice_quote(db.read_quotes_in_table(random.randint(1, db.count_id()))))

        return return_list_result(quotes)


@app.route('/api/post_json', methods=['POST'])
def requests_json():
    request_data = request.get_json()

    if 'author' and 'book_title' and 'quote' in request_data:
        author = request_data['author']
        book_title = request_data['book_title']
        quote = request_data['quote']

        return {
            'author': author,
            'boo_title': book_title,
            'quote': quote
        }
    
    return "Error"


app.run()
