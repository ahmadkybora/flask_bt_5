from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update, InlineKeyboardButton
from decouple import config

token = config("TOKEN")


def start(update: Update, context: CallbackContext):
    keyboards = [
        [InlineKeyboardButton('1', callback_data='salam_1'), InlineKeyboardButton('2', callback_data='salam_2')], 
        [InlineKeyboardButton('3', callback_data='salam_3'), InlineKeyboardButton('4', callback_data='salam_4')], 
        [InlineKeyboardButton('5', callback_data='salam_5'), InlineKeyboardButton('6', callback_data='salam_6')], 
        [InlineKeyboardButton('7', callback_data='salam_7'), InlineKeyboardButton('8', callback_data='salam_8')], 
    ]

    update.effective_message.reply_text('', reply_markup=keyboards)

def getVoice(update: Updater, context: CallbackContext):
    file = update.bot.get_file().download()


def main():
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()