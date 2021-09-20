# Модуль с функциями

from flask import jsonify
from db_admonistrate import DateBaseA

db = DateBaseA()


def give_a_nice_quote(info_for_quote):
    """Возвращает цитату в виде списка"""
    return {'ID': info_for_quote[0],
            'Author': info_for_quote[1],
            'Book title': info_for_quote[2],
            'Quote': info_for_quote[3]
            }


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
