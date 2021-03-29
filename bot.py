import telebot
import tokens
import datetime  # remove from the production version!
import time

bot = telebot.TeleBot(tokens.token)
previous_price = 0
delay = 5  # seconds
pause = bool()  # False


def get_prices():
    now = datetime.datetime.now()
    datum = now.strftime("%H:%M:%S")
    print(datum)
    return ['1000']  # prices


def main():
    global pause, previous_price
    if not pause:
        prices = get_prices()

        if len(prices) > 1:
            price = int(prices[clarify_the_ticket() - 1])  # Пользователь вводит номер нужного билета как ему удобно,
            # ... а у нас, программистов, всё начинается с 0, а не с 1
        else:  # Все остальные случаи:
            price = int(prices[0])

        if price < previous_price:
            print('Билеты подешевели')  # Тут будет вызов для бота...
            previous_price = price  # Перезапись цены, чтобы текущая стоимость билета для следующей была предыдущей
        if price > previous_price:
            print('Билеты подорожали')  # ... он будет выводит вот эту фразу и цену.
            previous_price = price
        time.sleep(delay)  # задержка в delay секунд
        main()  # рекурсия, после задержки, функция вызывает саму себя и процесс повторяется
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
        main()
    else:
        bot.send_message(message.from_user.id, "Прошу прощения, но я не понимаю, что Вы имеете в виду. Попробуйте использовать /help.")


# @handler_
def clarify_the_ticket():  # Уточнить номер билета, на случай, если он там не один
    id_of_the_ticket = 0
    return id_of_the_ticket


'''
https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty
'''

bot.polling(none_stop=True)
