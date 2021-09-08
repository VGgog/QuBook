# Парсит цитаты с сайта https://quote-citation.com/book

import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent



url = 'https://quote-citation.com/book'
quotes_author_and_book_name = []
count = 1
ua = UserAgent()
header = {'User-Agent': str(ua.chrome)}

for i in range(33):
    # Парсинг всех цитат с девяти страниц.
    url_page = url + '/page/' + str(i)
    response = requests.get(url_page, headers=header)
    print(response.status_code)
    bs = BeautifulSoup(response.text, 'lxml')

    quotes = bs.find('div', {'id': 'content'}).find_all('div', class_='quote')
    
    for info_of_quote in quotes:
        quote = info_of_quote.find('div', class_='quote-text').find('p').text
        author_and_book_name = info_of_quote.find('p', class_='source').find_all('a')
        try:
            author = author_and_book_name[0].text
            book_name = author_and_book_name[1].text
            quotes_author_and_book_name.append(
                {
                    'Автор': author,
                    'Название произведения': book_name,
                    'Цитата': quote
                }
            )
        except Exception as e:
            print(repr(e))
        print(count)
        count += 1

with open('quotes.json', 'a', encoding='utf-8') as file:
    json.dump(quotes_author_and_book_name, file, indent=4, ensure_ascii=False)

print('Всё готово!')
