import re


def get_prices():
    # prices = ['7 280 ₽', '10 546 ₽', '10 559 ₽']  # скопировал из консоли JS
    prices = ['7 280 ₽', '10 546 ₽', '10 559 ₽']  # прописал вручную
    # deleting the P from the elements of the list
    prices = [item[:-2] for item in prices]
    # prices = [item = ''.join(item.split()) for item in prices]
    prices = [int(item.replace(' ', '')) for item in prices]
    # for item in prices:
    #     item = re.sub(r'\s+', '', item)
    # prices = [item.translate({ord(c): None for c in string.whitespace}) for item in prices]
    return prices


print(get_prices())
