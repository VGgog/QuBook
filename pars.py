# Парсит цитаты с сайта https://quote-citation.com/book

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import psycopg2

connection = psycopg2.connect('''connection to db''')
cursor = connection.cursor()



url = 'https://quote-citation.com/book'
quotes_author_and_book_name = []
count = 1
ua = UserAgent()
header = {'User-Agent': str(ua.chrome)}

for i in range(33):
    # Парсинг всех цитат с девяти страниц.
    url_page = url + '/page/' + str(i)
    response = requests.get(url_page, headers=header)

    bs = BeautifulSoup(response.text, 'lxml')

    # Нахожу все цитаты с сайта
    quotes = bs.find('div', {'id': 'content'}).find_all('div', class_='quote')

    for info_of_quote in quotes:
        # Проходится по списку всех цитат, избавляет от тегов и добавляет по переменным
        quote = info_of_quote.find('div', class_='quote-text').find('p').text
        author_and_book_name = info_of_quote.find('p', class_='source').find_all('a')
        try:
            author = author_and_book_name[0].text
            book_name = author_and_book_name[1].text
            with connection.cursor() as cursor:
                # Добавляет цитаты в бд
                cursor.execute("""INSERT INTO quobook(id, author, "book name", quote) VALUES (%s, %s, %s, %s)""",
                               (count, author, book_name, quote))
                connection.commit()

        except Exception as e:
            connection.rollback()
            print(repr(e))

        print(count)
        count += 1

print('Всё готово!')
