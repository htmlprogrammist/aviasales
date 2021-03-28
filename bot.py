import telebot
import tokens
import app
import threading
import datetime

bot = telebot.TeleBot(tokens.token)
delay = 5
pause = bool()


def get_prices():
    global pause
    if not pause:
        threading.Timer(delay, get_prices).start()
        now = datetime.datetime.now()
        datum = now.strftime("%H:%M:%S")
        print(datum)
    else:
        pass
    return []


# @handler_
def clarify_the_ticket():  # Уточнить номер билета, на случай, если он там не один
    id_of_the_ticket = 0
    return id_of_the_ticket


def simulate_call():
    global pause
    get_prices()
    pause = bool(input())  # False => stops algorithm


pause = bool(input())
simulate_call()
