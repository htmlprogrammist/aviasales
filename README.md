# Ваш авиатор
## Ссылка
http://t.me/youraviatorbot

## Использование
1. Бот реагирует на команду **/start**;
2. Далее необходимо отправить ссылку на Ваш запрос в Яндекс.Путешествия (вкладка "Авиабилеты") и отправить **ссылку** на эту страницу боту;
3. Затем бот попросит Вас ввести номер билета *(сверху вниз)*. Если отображается всего один билет, введите "1";
4. Бот будет уведомлять Вас о том, что цена изменилась;
5. Чтобы остановить работу бота, введите команду **/stop**;
6. Если что-то непонятно, введите **/help**.

## Логика приложения
Представляет собой 2 функции:
1. `get_price()` - парсер, реализованный с использованием [webdriver](https://pypi.org/project/selenium/). Он дожидается, пока все объекты с классом `price` загрузятся на странице и возвращает список из этих объектов. Объекты в списке имеют тип `int`.
2. `main` - здесь содержится сравнение цен. Бот отправляет сообщение только при условии, что цена меняется. Номер билета передаётся из шага 3 в "Использование" (с технической точки зрения это функция `clarify_the_ticket()`). 

## Телеграм бот
Реагирует на команды:
- `/start` - начало работы с ботом. Сбрасывает значение `pause` на `False`, поэтому это необходимо прописывать **каждый раз**, начиная работать с ботом;
- `/stop` - завершить работу с ботом. Изменяет значение `pause` на `True`, чем останавливает **все** потоки, идущие от `main()`.
- `/help` - помощь

После введения команды `/start` он ожидает получить ссылку. В противном случае, бот выводит информацию о том, что пользователю нужно обратиться к `/help`.

Затем бот просит уточнить номер билета у пользователя. Номер билета считается сверху вниз, то есть первый билет = 1, второй билет = 2 и тд. В противном случае, придётся заново отправлять ссылку боту.

## Установка
1. Создайте файл `config.py`;
2. Создайте переменную `token` и в качестве значения используйте строку, содержащую API Token, полученный от Bot Father;
3. Создайте переменную `delay` и в качестве значения используйте натуральное число. Задержка указывается в секундах. По умолчанию это значение составляет 10 минут;
4. Введите `pip3 install -r requirements.txt`, чтобы установить необходимые библиотеки

## Примечание
Не стоит отправлять боту одну и ту же ссылку несколько раз. Библиотека `threading` создаёт то количество запросов, сколько раз была отправлена ссылка. Возможна ситуация, когда бот просто ляжет, дав слишком большую нагрузку на сервер своими запросами (или парсер перестанет передавать значения)

---
# Your aviator
## Link
http://t.me/youraviatorbot

## Usage
1. The bot responds to the **/start** command;
2. Next, you need to send a link to your request to Yandex.Travel (the "Flights" tab) and send a **link** to this page to the bot;
3. Then the bot will ask you to enter the ticket number *(from top to bottom)*. If only one ticket is displayed, enter "1";
4. The bot will notify you that the price has changed;
5. To stop the bot, enter the **/stop** command;
6. If something is not clear, enter **/help**.

## Application logic
Represents 2 functions:
1. `get_price()` is a parser implemented using [webdriver](https://pypi.org/project/selenium/). It waits for all objects with the `price` class to load on the page and returns a list of these objects. The objects in the list are of type `int`.
2. `main` - contains a price comparison. The bot sends a message only if the price changes. The ticket number is passed from step 3 in "Usage" (technically, this is the function `clarify_the_ticket()`).

## Telegram bot
Responds to commands:
- `/start` - start working with the bot. Resets the `pause` value to `False`, so this must be specified **every time** you start working with the bot;
- `/stop` - stop working with the bot. Changes the value of `pause` to `True`, which stops **all** threads coming from `main()`;
- `/help` - help.

After entering the `/start` command, it expects to get a link. Otherwise, the bot outputs information that the user needs to access `/help`.

The bot then asks the user to specify the ticket number. The ticket number is counted from top to bottom, i.e. first ticket = 1, second ticket = 2, etc. Otherwise, you will have to re-send the link to the bot.

## Installation
1. Create a file `config.py`;
2. Create the `token` variable and use the string containing the *API Token* received from Bot Father as the value;
3. Create the `delay` variable and use a natural number as the value. The delay is specified in *seconds*. By default, this value is 600 (10 minutes);
4. Enter `pip3 install -r requirements.txt` to install the required libraries.

## NB!
Do not send the same link to the bot several times. The `threading` library creates the number of requests that equals the number of times the link was sent by the user. There may be a situation when the bot simply lies down, giving too much load on the server with its' requests (or the parser stops transmitting values)
