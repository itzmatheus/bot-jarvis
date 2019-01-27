from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

from projeto.core.settings import TELEGRAM_TOKEN
from projeto.core.settings import DB_INTERFACE

class Bot(object):

    def run(self):
        # Create the Updater and pass it your bot's token.
        updater = Updater(token=TELEGRAM_TOKEN)

        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher

        # on different commands - answer in Telegram
        dispatcher.add_handler(
            CommandHandler('start', self.start)
        )
        dispatcher.add_handler(
            MessageHandler(Filters.command, self.unknown)
        )

        # Start the Bot
        updater.start_polling()
        print("Bot J.A.R.V.I.S Iniciado...")

        # Block until the user presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print("press CTRL + C to cancel.")
        updater.idle()


    def start(self, bot, update):
        response_message = "Olá, sou JARVIS"
        bot.send_message(
            chat_id=update.message.chat_id, text=response_message
        )
        print(bot, update)
    def unknown(self, bot, update):
        response_message = "Desculpe-me, não entendi!"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )
        print(bot, update)
