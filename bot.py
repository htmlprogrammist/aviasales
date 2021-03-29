import telebot
import tokens
import app

bot = telebot.TeleBot(tokens.token)


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
        bot.send_message(message.from_user.id, "Прекрасно! Я принял Вашу ссылку и готов работать.")
    else:
        bot.send_message(message.from_user.id, "Не понял...")


'''
https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c239&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c213&when=2021-04-03#empty
'''


# @handler_
def clarify_the_ticket():  # Уточнить номер билета, на случай, если он там не один
    id_of_the_ticket = 0
    return id_of_the_ticket


def simulate_call():
    global pause
    app.get_prices()
    pause = bool(input())  # False => stops algorithm


# pause = bool(input())
# simulate_call()

bot.polling(none_stop=True)
