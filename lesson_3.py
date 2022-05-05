import os
import json
import requests
from bs4 import BeautifulSoup


for count_url in range(1, 11):
    # print(f'Страница {count_url}')
    url = f"https://quotes.toscrape.com/page/{count_url}"
    req = requests.get(url)
    if req.status_code == 200:
        soup = BeautifulSoup(req.content, 'html.parser')
        all_quotes = soup.select('div[class=quote]')
        for quote in all_quotes:
            quotes = quote.select_one('span[class=text]').text.strip()
            # print(quotes)
            author = quote.select_one('small[class=author]').text
            # print(author)
            tags_in = quote.select('div[class=tags] a[class=tag]')
            tags = [tag.text for tag in tags_in]
            # print(tags)
            quote_dict = {
                'quote': quotes,
                'author': author,
                'tags': tags
            }
            with open('quotes.json', 'a', encoding='utf-8') as js:
                json.dump(quote_dict, js)
                js. write(',')
                js. write('\n')

# print(len(quotes_list))
# print(quotes_list)
