import re
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
# second parser
import lxml.html


def get_prices():

    URL_TEMPLATE = "https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty"
    r = requests.get(URL_TEMPLATE)
    time.sleep(10)
    print(r.status_code)
    # print(r.text)
    soup = bs(r.text, "html.parser")
    price_list = soup.find_all('span', class_='text')
    for price in price_list:
        print(price.text)

    # silenium
    # browser.get('http://playsports365.com/wager/OpenBets.aspx')
    # requiredHtml = browser.page_source


# get_prices()


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


def first_parser():
    # https://ru.stackoverflow.com/questions/1115181/beautiful-soup-не-парсит-всю-страницу
    url = "https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    html = driver.page_source
    soup = bs(html, "html.parser")
    price_list = soup.find_all('span', class_='text')
    for price in price_list:
        print(price.text)
# print(get_prices_list())


# first_parser()


def second_parser():
    # https://www.cyberforum.ru/python/thread2231305.html
    url = "https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty"
    resp = requests.get(url)
    print(resp.text)
    root = lxml.html.fromstring(resp.text)


second_parser()
