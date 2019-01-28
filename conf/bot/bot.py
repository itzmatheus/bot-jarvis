from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

from projeto.core.settings import TELEGRAM_TOKEN
from projeto.core.settings import DB_INTERFACE
from datetime import datetime

class Bot(object):

    #Variaveis para ativar funcionalidades
    _keys = {
        'echo':False
    }

    def run(self):
        # Create the Updater and pass it your bot's token.
        updater = Updater(token=TELEGRAM_TOKEN)

        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher

        dispatcher.add_handler(
            CommandHandler('start', self.start)
        )

        '''Mensagens Padroes'''
        dispatcher.add_handler(
            MessageHandler(Filters.text, self.echo)
        )
        dispatcher.add_handler(
            CommandHandler('echo', self.activate_echo)
        )
        '''Comandos'''
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
        response_message = "Olá, sou o J.A.R.V.I.S :)"
        bot.send_message(
            chat_id=update.message.chat_id, text=response_message
        )
        print("[{data}] BOT: {bot} | Usuario: {usuario} | Mensagem: '{msg}'".format(
            data=datetime.now().strftime("%d/%m/%y %H:%M:%S"),
            bot=bot.username,
            usuario=update.message.chat.first_name + ' ' + update.message.chat.last_name,
            msg=response_message))


    def activate_echo(self, bot, update):
        if not self._keys['echo']:
            response_message="Função /echo ativada!"
            self._keys['echo'] = True
        else:
            response_message="Função /echo desativada!"
            self._keys['echo'] = False
        bot.send_message(chat_id=update.message.chat_id, text=response_message)


    def echo(self, bot, update):
        if self._keys['echo']:
            response_message=update.message.text
            bot.send_message(chat_id=update.message.chat_id, text=response_message)
            print("[{data}] BOT: {bot} | Usuario: {usuario} | Mensagem: '{msg}'".format(
                data=datetime.now().strftime("%d/%m/%y %H:%M:%S"),
                bot=bot.username,
                usuario=update.message.chat.first_name + ' ' + update.message.chat.last_name,
                msg=response_message))
        else:
            pass


    #Default method to unkow command line bot
    def unknown(self, bot, update):
        response_message = "Desculpe-me, não entendi!"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )
        print("[{data}] BOT: {bot} | Usuario: {usuario} | Mensagem: '{msg}'".format(
            data=datetime.now().strftime("%d/%m/%y %H:%M:%S"),
            bot=bot.username,
            usuario=update.message.chat.first_name + ' ' + update.message.chat.last_name,
            msg=response_message))
