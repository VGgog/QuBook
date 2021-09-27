import random
import flask
from flask import request, jsonify

from db_administration import DateBaseA
import functions as func

db = DateBaseA()

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def home():
    """Домашняя страница"""
    return "<h1>Hello World!<h1>"


@app.route('/api/quobook', methods=['GET'])
def returns_a_specific_quote():
    """Возвращает определённую цитату, которую задал пользователь"""
    if request.args.get('count'):
        # Определяет количество цитат, которые нужны пользователю

        try:
            count = int(request.args['count'])
        except ValueError:
            return 'Error, count not faithful'
    else:
        count = 1

    if 'id' in request.args:
        # Возвращает цитату по id
        try:
            quote_id = int(request.args['id'])
        except ValueError:
            return 'Error, id not faithful'

        if db.read_quotes_in_table(quote_id):
            return jsonify(func.give_a_nice_quote(db.read_quotes_in_table(quote_id))), 200
        else:
            return 'Error, quote not found', 404


    elif 'author' in request.args:
        # Возвращает отсортированные по автору цитаты
        author = request.args.get('author')
        return func.return_list_result(func.return_sorted_quotes(count, author, index=1))

    elif 'book_title' in request.args:
        # Возвращает отсортированные по названию книги цитаты
        book_title = request.args.get('book_title')
        return func.return_list_result(func.return_sorted_quotes(count, book_title, index=2))

    else:
        # Возвращает случайные цитаты(количество задаёт пользователь)
        quotes = []
        while len(quotes) < count:
            quote_id = random.randint(1, db.count_id())
            if db.read_quotes_in_table(quote_id):
                quotes.append(func.give_a_nice_quote(db.read_quotes_in_table(random.randint(1, db.count_id()))))

        return func.return_list_result(quotes)


@app.route('/api/quobook/new', methods=['POST'])
def add_a_new_quote():
    """POST метод, записывает цитату, отправленную пользователем в таблицу QuoBook"""
    request_data = request.get_json()

    if 'Author' in request_data:
        if 'Book title' in request_data:
            if 'Quote' in request_data:
                request_data.setdefault('ID', db.count_id() + 1)
                db.write_new_quote_on_table(request_data)
                return func.give_a_nice_quote(request_data), 200

    return "Error, quote not write in db table"


@app.route('/api/quobook/del', methods=['DELETE'])
def delete_a_quote():
    """DELETE-methods, удаляет цитату по id"""
    if 'id' in request.args:
        # Возвращает цитату по id
        try:
            quote_id = int(request.args['id'])
        except ValueError:
            return 'Error, id not faithful'

        try:
            quote = func.give_a_nice_quote(db.read_quotes_in_table(quote_id))
            db.delete_quote(quote_id)
        except (TypeError, IndexError):
            return "Error, this quote not found"

        return quote

    return "Error, quote not found"


@app.route('/api/quobook/put', methods=['PUT'])
def update_or_add_new_quote():
    """"""
    request_data = request.get_json()

    if 'ID' in request_data:
        if 'Author' in request_data:
            if 'Book title' in request_data:
                if 'Quote' in request_data:
                    try:
                        quote_id = int(request_data['ID'])
                    except ValueError:
                        return 'Error, id not faithful'

                    if db.read_quotes_in_table(quote_id):
                        db.update_quote_in_table(request_data, quote_id)
                        return request_data
                    else:
                        db.write_new_quote_on_table(request_data)
                        return request_data

    else:
        return 'Put, Error'


app.run()
