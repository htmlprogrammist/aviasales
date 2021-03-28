import telebot
import tokens
import app

bot = telebot.TeleBot(tokens.token)


# @handler_
def clarify_the_ticket():  # Уточнить номер билета, на случай, если он там не один
    id_of_the_ticket = 0
    return id_of_the_ticket


def simulate_call():
    global pause
    app.get_prices()
    pause = bool(input())  # False => stops algorithm


pause = bool(input())
simulate_call()

bot.polling(none_stop=True, interval=0)
