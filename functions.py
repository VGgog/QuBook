# Модуль с функциями

from flask import jsonify
from db_administration import DateBaseA

db = DateBaseA()


def give_a_nice_quote(info_for_quote):
    """Возвращает цитату в виде списка"""
    if info_for_quote:
        if isinstance(info_for_quote, list) or isinstance(info_for_quote, tuple):
            info_for_quote = info_for_quote[0]
            return {'ID': info_for_quote[0],
                    'Author': info_for_quote[1],
                    'Book title': info_for_quote[2],
                    'Quote': info_for_quote[3]
                    }
        elif isinstance(info_for_quote, dict):
            return {'ID': info_for_quote['ID'],
                    'Author': info_for_quote['Author'],
                    'Book title': info_for_quote['Book title'],
                    'Quote': info_for_quote['Quote']
                    }
    else:
        return "Error, this quote not found"


def return_list_result(checklist):
    """Если в списке есть цитаты, то возвращает их, иначе возвращает 404"""
    if checklist:
        return jsonify(checklist), 200
    else:
        return 'Error, this author not found', 404


def return_sorted_quotes(count, sorting, index):
    """Возвращает список отсортированный по автору(index = 1) или по названию книги(index = 2) цитат"""
    sorted_quotes = []
    for information_for_quote in db.return_date_in_table():
        if len(sorted_quotes) < count:
            if sorting in information_for_quote[index]:
                sorted_quotes.append(give_a_nice_quote(information_for_quote))

    return sorted_quotes


def check_correct_data(data):
    """"""
    if 'Author' in data:
        if 'Book title' in data:
            if 'Quote' in data:
                return True

    return False

