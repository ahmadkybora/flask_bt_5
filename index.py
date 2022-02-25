from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update, InlineKeyboardButton
# from decouple import config
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
token = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"
# token = config("TOKEN")

# def start(update: Update, context: CallbackContext):
#     keyboards = [
#         [InlineKeyboardButton('1', callback_data='salam_1'), InlineKeyboardButton('2', callback_data='salam_2')], 
#         [InlineKeyboardButton('3', callback_data='salam_3'), InlineKeyboardButton('4', callback_data='salam_4')], 
#         [InlineKeyboardButton('5', callback_data='salam_5'), InlineKeyboardButton('6', callback_data='salam_6')], 
#         [InlineKeyboardButton('7', callback_data='salam_7'), InlineKeyboardButton('8', callback_data='salam_8')], 
#     ]

#     update.effective_message.reply_text('ss', reply_markup=keyboards)

# def getVoice(update: Updater, context: CallbackContext):
#     file = update.bot.get_file().download()


def getFile(update: Update, context: CallbackContext):
    text = update.message.text
    file = context.bot.sendDocument(update.effective_chat.id, text)
    context.bot.sendMessage(file)

def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, getFile))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()