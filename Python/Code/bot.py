#This script is independet of lib or python version (tested on python 2.7 and 3.5)
TOKEN = '675366007:AAGdYIBhgJwks2dv1zs-14KSwt-RXUzSbH4'

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler 
from telegram.ext import MessageHandler
from telegram.ext import Filters
import random


ids = []

#sends the info of what is DSC
def startA(bot: Bot, update: Update):
    bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def comprobarNuevo(bot: Bot, update: Update):
    text = update.message.text
    usuario = bot.get_chat_member(update.message.chat.id,)
    if "c" in text:
        bot.send_message(
                chat_id = update.effective_chat.id,
                text = usuario,
            )


def main():

    bot = Bot(
            token = TOKEN,
        )
    updater = Updater(
            bot = bot,
        )

    start_handler = CommandHandler("start", startA)
    ee_handler = MessageHandler(Filters.text, comprobarNuevo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(ee_handler)
    

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()