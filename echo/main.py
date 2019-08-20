from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import sqlite3

from config import TG_TOKEN
from config import foo


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Отправь мне своё имя",
    )


def do_echo(bot: Bot, update: Update):
    text = update.message.text
    list = foo(text)
    res = text + ', во время игры ты будешь сидеть за следующими столами: \n'
    for i in list:
        res += '\t' + 'Тур ' + str(i[1] + 1) + ': ' + 'стол ' + str(i[0] + 1) + '\n'
    bot.send_message(
        chat_id=update.message.chat_id,
        text=res,
    )


def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,
    )
    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
