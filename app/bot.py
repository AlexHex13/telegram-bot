from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

button_help = 'Help'


def message_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help),
            ],
        ],
        resize_keyboard=True
    )
    update.message.reply_text(
        text='Hello Click me!',
        reply_markup=reply_markup,
    )


def main():
    updater = Updater(
        token='1355498746:AAGMcqGmbOhP0_qs2DVDIsfhTLkI1I1BQQQ',
        use_context=True
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
