import json

from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://market.yandex.ru/partners/news'

request = requests.get(url)

result = request.content

soup = BeautifulSoup(result, 'lxml')

news = soup.find_all('div', class_='news-list__item')

with open('yandex/index_yandex.txt', 'w', encoding='utf-8') as f:
    for i in news:
        href = i.find('a').get('href')
        f.write(f'https://market.yandex.ru{href}\n')


def get_data_yandex(file):
    with open(file) as f:
        urls_list = [line.strip() for line in f.readlines()]
    articles = []
    s = requests.Session()

    for url in enumerate(urls_list[:10]):
        response = s.get(url=url[1])
        soup = BeautifulSoup(response.text, 'lxml')
        article_title = soup.find('div', class_='news-info__title').text.strip()
        article_text = soup.find('div', class_='news-info__post-body html-content page-content').text.strip()
        article_tag = soup.find('div', class_='news-info__tags').text.strip().split('#')
        article_date = soup.find('time').get('datetime')[:10]

        articles.append(
            {
                'name': article_title,
                'description': article_text,
                'tags': article_tag,
                'tag_news': 'yandex',
                'date': article_date,

            }
        )
        print(f'Обработано {url[0] + 1}')

    with open('yandex_json/article_yandex.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)

def main():
    get_data_yandex('yandex/index_yandex.txt')


if __name__ == '__main__':
    main()
