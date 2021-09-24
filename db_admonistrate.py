from connection import connect

import psycopg2


class DateBaseA:
    def __init__(self):
        self.connection = psycopg2.connect(database="QuoBook",
                                      user="postgres",
                                      password=connect,
                                      host="127.0.0.1",
                                      port="5432")
        self.cursor = self.connection.cursor()

    def read_quotes_in_table(self, quote_id):
        """Возвращает строку из таблицы QueBook"""
        self.cursor.execute('SELECT * FROM QuoBook WHERE QuoBook.Id = %s', (quote_id,))
        return self.cursor.fetchall()[0]

    def write_new_quote_on_table(self, quote_info):
        """Записывает новую цитату в таблицу QueBook"""
        self.cursor.execute("""INSERT INTO QuoBook(id, author, "book name", quote) VALUES (%s, %s, %s, %s)""",
                                   (quote_info['ID'], quote_info['Author'], quote_info['Book title'], quote_info['Quote']))
        return self.connection.commit()

    def change_quote_in_table(self):
        pass

    def delete_quote(self, quote_id):
        """Удаляет нужную строку из таблицы QueBook"""
        self.cursor.execute("DELETE FROM QuoBook WHERE QuoBook.Id = %s", (quote_id,))
        return self.connection.commit()

    def count_id(self):
        """Выводит количество строк в таблицу QuoBook"""
        self.cursor.execute("""SELECT COUNT(*) FROM QuoBook;""")
        return self.cursor.fetchone()[0]

    def return_date_in_table(self):
        """"""
        self.cursor.execute("SELECT * FROM QuoBook")
        return self.cursor.fetchall()
