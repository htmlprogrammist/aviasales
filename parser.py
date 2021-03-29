import re
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver


def get_prices():

    URL_TEMPLATE = "https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty"
    r = requests.get(URL_TEMPLATE)
    print(r.status_code)
    # print(r.text)
    soup = bs(r.text, "html.parser")
    price_list = soup.find_all('span', class_='price')
    for price in price_list:
        print(price.text)

    # silenium
    # browser.get('http://playsports365.com/wager/OpenBets.aspx')
    # requiredHtml = browser.page_source


get_prices()


def get_prices_list():
    # prices = ['7 280 ₽', '10 546 ₽', '10 559 ₽']  # скопировал из консоли JS
    prices = ['7 280 ₽', '10 546 ₽', '10 559 ₽']  # прописал вручную
    # deleting the P from the elements of the list
    prices = [item[:-2] for item in prices]
    # prices = [item = ''.join(item.split()) for item in prices]
    prices = [int(item.replace(' ', '')) for item in prices]
    # for item in prices:
    #     item = re.sub(r'\s+', '', item)
    # prices = [item.translate({ord(c): None for c in string.whitespace}) for item in prices]
# Не удаляю комментарии из функции, потому что пока неясно, как себя поведёт парсер, когда получит значения и запихнёт
# их внутрь prices


# print(get_prices_list())


