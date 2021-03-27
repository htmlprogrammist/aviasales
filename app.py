def get_price():
    return 0


def main():
    global previous_price
    price = get_price()
    if previous_price == price:
        pass
    if price < previous_price:
        print('Билеты подешевели')  # Тут будет вызов для бота...
        previous_price = price  # Перезапись цены, чтобы текущая стоимость билета для следующей была предыдущей
    if price > previous_price:
        print('Билеты подорожали')  # ... он будет выводит вот эту фразу и цену.
        previous_price = price
    return previous_price
