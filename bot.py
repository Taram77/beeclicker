from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    web_app_url = "46.229.215.156"
    keyboard = [[InlineKeyboardButton("Открыть приложение", web_app={"url": web_app_url})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Нажмите на кнопку ниже, чтобы открыть приложение:', reply_markup=reply_markup)

def main():
    updater = Updater("<Ваш-Токен>", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
