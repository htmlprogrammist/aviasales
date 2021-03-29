import telebot
import tokens
import datetime  # remove from the production version!
import time
import threading

bot = telebot.TeleBot(tokens.token)
previous_price = 0
delay = 5  # seconds
pause = bool()  # False


def get_prices():
    now = datetime.datetime.now()
    datum = now.strftime("%H:%M:%S")
    print(datum)
    return ['1000']  # prices


def main(message):
    global pause, previous_price
    if not pause:
        prices = get_prices()

        if len(prices) > 1:
            price = int(prices[clarify_the_ticket(message) - 1])  # Пользователь вводит номер нужного билета как ему удобно,
            # ... а у нас, программистов, всё начинается с 0, а не с 1
        else:  # Все остальные случаи:
            price = int(prices[0])

        if price < previous_price:
            print('Билеты подешевели')  # Тут будет вызов для бота...
            previous_price = price  # Перезапись цены, чтобы текущая стоимость билета для следующей была предыдущей
        if price > previous_price:
            print('Билеты подорожали')  # ... он будет выводит вот эту фразу и цену.
            previous_price = price
        threading.Timer(delay, main).start()
        return previous_price


@bot.message_handler(commands=['start'])
def get_start_message(message):
    bot.send_message(message.from_user.id, "Здравствуйте, я Ваш авиатор. Отправьте мне ссылку на Ваш билет из Яндекс.Путешествия")


@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.from_user.id,
                     '''Если Вы не знаете, как отправить мне ссылку на билет, то следуйте следующей инструкции:
- Откройте сайт "Яндекс.Путешествия"
- Выберите "Авиабилеты"
- Определите город и дату для поиска билетов, затем нажмите кнопку "Найти"
- Вы перейдёте по ссылке, по которой и будете смотреть билеты. Скопируйте эту ссылку и отправьте мне.''')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text[8:21] == "travel.yandex":
        bot.send_message(message.from_user.id, "Прекрасно! Я принял Вашу ссылку и принимаюсь за работу.")
        main()  # вынужденная мера передавать в main() переменную message.
        # Я уверен, что с производительностью могут быть проблемы, но на этом проекте это будет не критично
    else:
        bot.send_message(message.from_user.id, "Прошу прощения, но я не понимаю, что Вы имеете в виду. Попробуйте использовать /help.")


# Уточнить номер билета, на случай, если он там не один
@bot.message_handler(content_types=['text'])
def clarify_the_ticket(message):
    try:
        if int(message.text):
            bot.send_message(message.from_user.id, "Хорошо, спасибо. Продолжаю работать. ")
            return int(message.text)
    except ValueError:
        bot.send_message(message.from_user.id, "Необходимо было ввести число. Попробуйте снова.")


'''
https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty
'''

bot.polling(none_stop=True)
