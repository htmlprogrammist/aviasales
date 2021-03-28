import bot

previous_price = 0


def main():
    global previous_price
    prices = get_prices()

    if len(prices) > 1:
        price = prices[bot.clarify_the_ticket() - 1]  # Пользователь вводит номер нужного билета как ему удобно,
        # ... а у нас, программистов, всё начинается с 0, а не с 1
    else:  # Все остальные случаи:
        price = prices[0]  # ... это просто [1000]

    if price < previous_price:
        print('Билеты подешевели')  # Тут будет вызов для бота...
        previous_price = price  # Перезапись цены, чтобы текущая стоимость билета для следующей была предыдущей
    if price > previous_price:
        print('Билеты подорожали')  # ... он будет выводит вот эту фразу и цену.
        previous_price = price
    return previous_price
