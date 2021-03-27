import bot


def get_prices():
    return []


def main():
    global previous_price
    prices = get_prices()

    if len(prices) > 1:
        price = prices[bot.clarify_the_ticket()]
    else:
        price = prices[0]

    if price < previous_price:
        print('Билеты подешевели')  # Тут будет вызов для бота...
        previous_price = price  # Перезапись цены, чтобы текущая стоимость билета для следующей была предыдущей
    if price > previous_price:
        print('Билеты подорожали')  # ... он будет выводит вот эту фразу и цену.
        previous_price = price
    return previous_price
