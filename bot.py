from distutils.log import info
import logging
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import Updater, CallbackContext, CallbackQueryHandler, MessageHandler, Filters
from telegram import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    KeyboardButton
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

token = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"

class Bot:

    def main():
        updater = Updater(token, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(MessageHandler(Filters.text, Bot.start))

        updater.start_polling()
        updater.idle()

    def start(update: Update, context: CallbackContext):
        i = [
            [InlineKeyboardButton('username', url='google.com', callback_data='1'), InlineKeyboardButton('2', url='google.com')],
        ]
        information = ReplyKeyboardMarkup(
            keyboard=i, 
            resize_keyboard=True, 
            input_field_placeholder="hello"
        )
        update.message.reply_text("salam", reply_markup=information)
        
if __name__ == '__main__':
    Bot.main()