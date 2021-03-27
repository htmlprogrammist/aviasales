# Your aviator - Telegram bot
## Main app logic (app.py)
It has several functions:
1. `get_price()` - to get the price using the parser. Returns an integer (variable `price`).
2. `main` - the main function, it contains the call to the previous function. It is called from `bot.py`. Accepts the global variable `previous_price`: it contains the previous price of the tickets. If the current price and the previous one are the same, the last does not change. Returns an integer (variable `previous_price`).
## Telegram bot logic (bot.py)
A simple bot. Controlled by the `/start` and `/stop` commands. It only responds to the ticket link that the user sends it. For example: `https://travel.yandex.ru/avia/search/result/?adult_seats=1&children_seats=0&fromId=c54&infant_seats=0&klass=economy&oneway=1&return_date=&toId=c44&toName=%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA&when=2021-03-30`. Otherwise, it will ask you to send this link, and it will not accept anything else.

After that, it will call `app.main ()` every N minutes to check how the price has changed.