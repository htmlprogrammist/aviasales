import telebot
import tokens
import datetime  # remove from the production version!
import time
import threading

bot = telebot.TeleBot(tokens.token)
previous_price = 0
delay = 5  # seconds
pause = bool()  # False
id_of_the_ticket = 0


def get_prices():
    now = datetime.datetime.now()
    datum = now.strftime("%H:%M:%S")
    print(datum)
    return ['1000', '1200', '1300']  # prices


def main():
    global pause, previous_price, id_of_the_ticket
    if not pause:
        prices = get_prices()
        price = int(prices[id_of_the_ticket])
        if price < previous_price:
            print('Билеты подешевели')  # Тут будет вызов для бота...
            previous_price = price  # Перезапись цены, чтобы текущая стоимость билета для следующей была предыдущей
        if price > previous_price:
            print('Билеты подорожали')  # ... он будет выводит вот эту фразу и цену.
            previous_price = price
        threading.Timer(delay, main).start()
        return previous_price


# Приветствие
@bot.message_handler(commands=['start'])
def get_start_message(message):
    bot.send_message(message.from_user.id, "Здравствуйте, я Ваш авиатор. Отправьте мне ссылку на Ваш билет из Яндекс.Путешествия")


# Помощь
@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.from_user.id,
                     '''Если Вы не знаете, как отправить мне ссылку на билет, то следуйте следующей инструкции:
- Откройте сайт "Яндекс.Путешествия"
- Выберите "Авиабилеты"
- Определите город и дату для поиска билетов, затем нажмите кнопку "Найти"
- Вы перейдёте по ссылке, по которой и будете смотреть билеты. Скопируйте эту ссылку и отправьте мне.''')


# Остановка работы
@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global pause
    pause = True  # функция main() больше не пашет
    bot.send_message(message.from_user.id, "Был рад служить. Надеюсь, был Вам полезен.")


# Основная логика работы бота
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global pause
    if message.text[8:21] == "travel.yandex" and not pause:
        bot.send_message(message.from_user.id, "Прекрасно! Я принял Вашу ссылку, осталось только уточнить номер билета (сверху вниз). Если билет один, то отправьте число 1.")
        pause = False  # сброс значения паузы, чтобы функция main снова могла работать
        bot.register_next_step_handler(message, clarify_the_ticket)  # Ожидаю, пока пользователь введёт сообщение с числом, потом вызывается функция clarify...
    else:
        bot.send_message(message.from_user.id, "Прошу прощения, но я не понимаю, что Вы имеете в виду. Попробуйте использовать /help.")


# Уточнение номера билета, на случай, если он там не один
@bot.message_handler(content_types=['text'])
def clarify_the_ticket(message):
    global id_of_the_ticket
    try:
        id_of_the_ticket = int(message.text) - 1
        bot.send_message(message.from_user.id, "Хорошо, спасибо. Начинаю работать.")
        main()
    except ValueError:
        bot.send_message(message.from_user.id, "Прошу прощения, но нужно было ввести номер билета. Давайте начнём всё сначала: отправьте ссылку повторно.")


'''
https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty
'''

bot.polling(none_stop=True)
