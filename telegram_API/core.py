import telebot
from telebot import types
from settings import SiteSettings
from site_API.core import CreateItemsInterface
from database.core import crud
from database.common.models import db, History

db_write = crud.create()
db_read = crud.retrieve()

core_api = CreateItemsInterface()
get_items = core_api.get_items()
phones: dict = get_items(min_price=100, max_price=1500, page=1)

site = SiteSettings()

token = site.bot_token.get_secret_value()

bot = telebot.TeleBot(token)

retrieved = db_read(db, History, History.price, History.item_name)


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     for key in phones.keys():
#         line_url = phones[key]['item_url']
#         print(line_url)
#         bot.send_message(message.chat.id, line_url)


def greetings():
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Начать работу бота")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "👋 Привет! Я бот который ищет мобильные телефоны на сайте aliexpress!",
                         reply_markup=markup)


def show_history():
    @bot.message_handler(commands=['history'])
    def response(message):
        bot.send_message(message.from_user.id, 'Ранее вы искали данные телефоны')
        bot.send_message(message.from_user.id, retrieved)


def menu():
    @bot.message_handler(content_types=['text'])
    def response(message):
        if message.text == '👋 Начать работу бота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            sort_btn_min = types.KeyboardButton('Сначала дешевые')
            sort_btn_max = types.KeyboardButton('Сначала дорогие')
            markup.row(sort_btn_min, sort_btn_max)
            sort_btn_between = types.KeyboardButton('Выбрать минимальную и максимальную стоимость')
            markup.row(sort_btn_between)
            bot.send_message(message.from_user.id, "Выберите как отсортировать результаты", reply_markup=markup)

        elif message.text == 'Сначала дешевые':
            bot.send_message(message.from_user.id, 'выбран пункт ДЕШЕВЫХ телефонов')
        elif message.text == 'Сначала дорогие':
            bot.send_message(message.from_user.id, 'выбран пункт ДОРОГИХ телефонов')
        elif message.text == 'Выбрать минимальную и максимальную стоимость':
            bot.send_message(message.from_user.id, 'выбран пункт поиска МЕЖДУ границами цены')


def start_bot():
    bot.infinity_polling()


class TelegramInterface:
    @staticmethod
    def start():
        return start_bot

    @staticmethod
    def menu():
        return menu

    @staticmethod
    def show_history():
        return show_history

    @staticmethod
    def greetings():
        return greetings


if __name__ == '__main__':
    TelegramInterface()
