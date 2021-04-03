from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_prices():
    chromedriver = '/Users/htmlprogrammist/Downloads/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    browser.get("https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c1094&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-08")

    try:
        element = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price"))
        )
        # print(int(element.text[:5]) + 1)  # ValueError: invalid literal for int() with base 10: '4\u2006780'
        print(element.text[:5])
    finally:
        browser.quit()
