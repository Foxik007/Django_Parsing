import json
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    try:
        driver = webdriver.Chrome('chromedriver.exe',options=options)
        driver.get(url=url)
        sleep(5)
        with open('ozon/index_selenium.html','w') as f:
            f.write(driver.page_source)
    except Exception as _ex:
        print(_ex)

def get_href():
    with open('ozon/index_selenium.html') as f:
        data = f.read()
    soup = BeautifulSoup(data, 'lxml')
    news = soup.find_all('div', class_='news-card')
    with open('ozon/ozon_href.txt', 'w') as f:
        for item in news:
            href = item.find('a').get('href')
            f.write(f'https://seller.ozon.ru{href}\n')
from selenium.webdriver.common.by import By


def get_html_ozon():
    with open('ozon/ozon_href.txt') as f:
        urls_list = [line.strip() for line in f.readlines()]
    options = webdriver.ChromeOptions()
    articles = []
    s = requests.Session()

    for url in urls_list:
        try:
            driver = webdriver.Chrome('chromedriver.exe',options=options)
            driver.get(url=url)
            sleep(1)

            article_title = driver.find_element(By.TAG_NAME,'h1').text
            article_text = driver.find_element(By.CLASS_NAME,'new-section').text
            article_tags = driver.find_element(By.CLASS_NAME, 'page-info__topic-value').text.split()
            # Понять как выгрузить дату из script
            #article_date = driver.find_element(By., '/html/body/script[1]/text()???? ').text.split()

            articles.append(
                {
                    'name': article_title,
                    'description': article_text,
                    'tags': article_tags,
                    'tag_news': 'ozon',
                    'date':'2022-08-27',

                }
            )
            print('Обработано}')

        except Exception as _ex:
            print(_ex)

        with open('ozon_json/article_ozon.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=4, ensure_ascii=False)

def main():
    get_data_with_selenium('https://seller.ozon.ru/news/')
    get_href()
    get_html_ozon()


if __name__ == '__main__':
    main()
