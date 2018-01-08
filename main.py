from telegram.ext import Updater, CommandHandler
from time import sleep
from binanceConnect import get_assets_list
import env
import threading
import requests

token = env.token

current_assets_list = get_assets_list()


def start(bot, update):
    update.message.reply_text('Welcome!')
    help(bot, update)


def help(bot, update):
    update.message.reply_text('/current - показать список валют на данный момент')


def current(bot, update):
    update.message.reply_text(
        'Валюты на данный момент: {0}'.format(
            str(get_assets_list()[:-1]).replace("[", "").replace("]", "").replace("(", "").replace(")", "")))


def telebot():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("current", current))
    updater.start_polling()


def get_assets():
    while True:
        # get data from API
        new_assets_list = get_assets_list()
        # check all assets
        for asset_in_new in new_assets_list:

            # if asset not in first assets's array
            if asset_in_new not in current_assets_list:

                for chat_id in env.chat_ids:
                    # log
                    print('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text="Новая валюта - {2}"'.format(
                        token, chat_id,
                        asset_in_new))
                    # send message to chat
                    requests.get(
                        'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text="Новая валюта - {2}'.format(
                            token, chat_id,
                            asset_in_new))
                    current_assets_list.append(asset_in_new)
        sleep(60)


if __name__ == '__main__':
    t1 = threading.Thread(name="Telegram Bot", target=telebot)
    t2 = threading.Thread(name="Get data from API", target=get_assets)
    print("Подключение с Binance установлено!")
    t1.start()
    t2.start()
