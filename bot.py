import telebot
import tokens
import app

bot = telebot.TeleBot(tokens.token)


# @handler_
def clarify_the_ticket():  # Уточнить номер билета, на случай, если он там не один
    id_of_the_ticket = 0
    return id_of_the_ticket
