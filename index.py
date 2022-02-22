from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import (
    Update, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    KeyboardButton, 
    InputInvoiceMessageContent
)
from decouple import config

token = config("TOKEN")


def getVoice(update: Updater, context: CallbackContext):
    file = update.bot.get_file().download()

def main():
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler()