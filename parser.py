import re
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
# second parser
import lxml.html


# https://stackoverflow.com/questions/59304608/how-to-solve-timed-out-error-when-using-requests-with-beautifulsoup


def get_prices():
    chromedriver = '/Users/htmlprogrammist/Downloads/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    browser.get("https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty")
    price = browser.find_element_by_class_name('price')
    print(price)
# def get_prices():
#     URL_TEMPLATE = "https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty"
#     r = requests.get(URL_TEMPLATE, timeout = (1000, 12000))
#     print(r.status_code)
#     # print(r.text)
#     soup = bs(r.text, "html.parser")
#     price_list = soup.find_all('span', class_='text')
#     print(price_list)
    # for price in price_list:
    #     print(price.text)

    # silenium
    # browser.get('http://playsports365.com/wager/OpenBets.aspx')
    # requiredHtml = browser.page_source


get_prices()


def ruslan_parser():
    url = "https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c1094&infant_seats=0&klass=economy&oneway=2&return_date=2021-05-08&toId=c213&utm_campaign=ssa_brand.travel_ru_all_new_11909513015&utm_content=k50id%7Ckwd-306418496100%7Ccid%7C11909513015%7Caid%7C488100031827%7Cgid%7C119481951270%7Cpos%7C%7Csrc%7Cg_%7Cdvc%7Cc%7Creg%7C1011927%7Crin%7C%7C&utm_medium=search&utm_source=google&utm_term=%2B%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%20%2B%D0%BF%D1%83%D1%82%D0%B5%D1%88%D0%B5%D1%81%D1%82%D0%B2%D0%B8%D1%8F&when=2021-03-31"
    r = requests.get(url=url, timeout=(3.05, 27))
    soup = bs(r.text, "html.parser")
    price_list = soup.find_all('span', class_='price')
    print(price_list)
    # for price in price_list:
    #     print(price.text)


ruslan_parser()


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
    # print(resp.text)
    root = lxml.html.fromstring(resp.text)
    print(root)


# second_parser()


def third_parser():
    # https://ru.stackoverflow.com/questions/1195327/Парсинг-stackoverflow-com-с-помощью-beautiful-soup?rq=1
    url = "https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty"
    answ_page = requests.get(url)
    answ_soup = bs(answ_page.text, 'html.parser')
    # print(answ_soup)  # <Element html at 0x7fa8a3a77d60>
    price_list = answ_soup.find_all('span', class_='price')
    for price in price_list:
        print(price.text)


# third_parser()
"""
GET /api/avia/search/results HTTP/1.1
Accept: application/json, text/plain, */*
Pragma: no-cache
Cookie: CSRF-TOKEN=4ccd3931447fe60d52a3578d6c9f7ab9303d666e%3A1617117910; ya-travel-avia-search-sort=:a; ya_travel_togglers=%7B%22MIR_POSSIBLE_CASHBACK_SEARCH%22%3Atrue%2C%22MIR_POSSIBLE_CASHBACK_HOTEL%22%3Atrue%2C%22MIR_CASHBACK_HOTEL%22%3Atrue%2C%22ADBLOCK_IS_ENABLED%22%3Afalse%7D; ya_travel_uid=eyJ5YVRyYXZlbFNlc3Npb25VaWQiOiJjOGQ2ZGU2NC1hYzcyLTQ5M2QtOTg1MS0xMDIzZTQzYzNjNTcifQ==; ya_travel_uid.sig=vbL7P6Cw2csux4gMRv7YOT7xvoU; yp=1641535319.ygu.1#1632869008.szm.2%3A1440x900%3A1440x837#1641714158.stltp.serp_bk-map_1_1610178158#1927122554.multib.1#1931715698.udn.cDrQldCz0L7RgCDQn9C%2B0YHRgtC40YDQvtC90LjQvQ%3D%3D#1929004108.2fa.1#1619779413.csc.1#1617707195.mcv.0#1617707195.mct.null#1617707195.mcl.z2fo29; ys=wprid.1617117645522672-663029516480396853945969-prestable-app-host-sas-web-yp-109; yabs-frequency=/5/000J0000003s3cDW/EcgmS9K0000eG24NKa5jXW0002X09m00/; cycada=Y1luIBFZ35361MwqgKdyvp+XSwJikEddeo/B0ONeNfM=; my=YwA=; zm=m-white_bender_zen-ssr.css-https%3As3home-static_yv_btWQsOHuI4d2WWabthZ5s5OU%3Al; Session_id=3:1616926971.5.0.1613489647749:HbqxUQ:4.1|359781741.2866051.2.2:2866051|1362253205.154461.2.2:154461|232279.173041.lQIQ83chfBj4vTqm7H2KRuqRRMg; sessionid2=3:1616926971.5.0.1613489647749:HbqxUQ:4.1|359781741.2866051.2.2:2866051|1362253205.154461.2.2:154461|232279.811334.2s2u68gA0lEaYUdQMxOK6cJam1U; yandex_login=eg.badmaev; utms=%7B%22utm_source%22%3A%22yandex_organic%22%7D; i=/lmyHwiqboxwGi0Nbg//5zkrWES03QzJrsSvU3kN284hG140aQMUS5MoIU9shRdZGBpt1ZyWfRkEQ1/+YGvbwH/anfk=; L=QkpIAnpED0AJAmJed0N5CVJ3cXsJfXV2LQNdLjclHjs/IQ==.1616355698.14547.393964.b1d12555a6f420a5814e6fe4bc4a9baf; experiment__enableHotelSearchPage=1; experiment__enableHotelsGeoRegionApp=1; experiment__enableHotelsSearchPage=1; experiment__enablePartnersFilter=; experiment__hotelsBookPage=1; experiment__isAviaPortal=; experiment__skipSalesCheck=; ya_travel_attribution_monthly=%7B%7D; yandex_gid=1094; mda=0; fuid01=5f99ea76260f030b.qpuj5w0iFlC55vwLyFjrxCGzzrO6GgQuN9YWflUDU5bKr56RGEEvIfLeQr2lHKK5OTvfnR4YhDXM6dE9NjTvf3Y70qXwFzIM-5yr5HpB3WxdC0OhME21IVRVolSA6v0k; yandexuid=5239046641600178707; yuidss=5239046641600178707; is_gdpr=0; is_gdpr_b=CKjwdxD1AygC; ymex=1915538709.yrts.1600178709
Accept-Encoding: gzip, deflate, br
Host: travel.yandex.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15
Accept-Language: ru
Referer: https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c213&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c1094&when=2021-04-03
Connection: keep-alive
"""
