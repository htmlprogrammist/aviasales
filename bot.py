import telebot
import config
import threading
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

bot = telebot.TeleBot(config.token)
previous_price = 0
delay = config.delay
pause = bool()  # False
id_of_the_ticket = 0
link = ''
user = 0


def get_prices(url):
    prices = []
    options = Options()
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), chrome_options=options)
    browser.get(url)

    try:
        price_list = WebDriverWait(browser, 30).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "price"))
        )  # парсинг всех элементов с классом 'price'. Возвращает list
        for i in range(len(price_list)):  # обработка полученного price_list
            price = ''.join(price_list[i].text.split('\u2006'))
            price = price[:-1]  # убираю последний символ: "Рубль"
            prices.append(int(price))
        print(prices)
        return prices
    finally:
        browser.quit()


def main():
    global pause, previous_price, id_of_the_ticket, link, user
    if not pause:
        prices = get_prices(link)
        prices = map(int, prices)
        # price = int(prices[id_of_the_ticket])
        price = min(prices)
        if price < previous_price:
            previous_price = price  # Перезапись цены, чтобы текущая стоимость билета для следующей была предыдущей
            bot.send_message(user,
                             "Цена на билет снизилась. Текущая стоимость составляет {0} рублей. Если Вы желаете "
                             "остановить меня, введите команду /stop".format(previous_price))
        if price > previous_price:
            previous_price = price
            bot.send_message(user,
                             "Цена на билет поднялась. Текущая стоимость составляет {0} рублей. Если Вы желаете "
                             "остановить меня, введите команду /stop".format(previous_price))
        threading.Timer(delay, main).start()
        return previous_price


# Приветствие
@bot.message_handler(commands=['start'])
def get_start_message(message):
    global pause, user
    bot.send_message(message.from_user.id, "Здравствуйте, я Ваш авиатор. Отправьте мне ссылку на Ваш билет из "
                                           "Яндекс.Путешествия")
    user = message.from_user.id  # передаю id пользователя, чтобы потом отправлять сообщения через функцию,
    # содержащую в себе логику работы
    pause = False  # сброс значения паузы, чтобы функция main снова могла работать


# Помощь
@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.from_user.id,
                     '''Инструкция:
- Откройте сайт "Яндекс.Путешествия"
- Выберите "Авиабилеты"
- Определите город и дату для поиска билетов, затем нажмите кнопку "Найти"
- Отправьте мне номер билета в списке, который Вы видите. Например, если Вам нужен первый билет, отправьте 1, если второй - 2.
- Скопируйте ссылку на страницу, на которой Вы сейчас находитесь, и отправьте мне.

Команды:
/start - начать работу со мной
/stop - завершить работу со мной
/help - помощь''')


# Остановка работы
@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global pause
    pause = True  # функция main() больше не работает
    bot.send_message(message.from_user.id, "Был рад служить. Надеюсь, был Вам полезен.")


# Основная логика работы бота
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global pause, link
    if message.text[8:21] == "travel.yandex" and not pause:
        bot.send_message(message.from_user.id, "Прекрасно! Я принял Вашу ссылку, осталось только уточнить номер "
                                               "билета (сверху вниз). Если билет один, то отправьте число 1.")
        link = message.text
        # bot.register_next_step_handler(message, clarify_the_ticket)
        # Ожидаю, пока пользователь введёт сообщение с числом, потом вызывается функция clarify_the_ticket()
    else:
        bot.send_message(message.from_user.id, "Прошу прощения, но я не понимаю, что Вы имеете в виду. Попробуйте "
                                               "использовать /help.")


# Уточнение номера билета
@bot.message_handler(content_types=['text'])
def clarify_the_ticket(message):
    global id_of_the_ticket
    try:
        # id_of_the_ticket = int(message.text) - 1
        id_of_the_ticket = 0
        main()
    except ValueError:
        bot.send_message(message.from_user.id, "Прошу прощения, но нужно было ввести номер билета. Давайте начнём всё "
                                               "сначала: отправьте ссылку повторно.")


bot.polling(none_stop=True)
