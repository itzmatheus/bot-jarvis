from conf.db.db_interface import DBConnect
import os
from dotenv import load_dotenv
load_dotenv()

"""
Sessao do Banco
"""

DB_CONFIG = (
    {
    'host':os.getenv("HOST"),
    'port':os.getenv("PORT"),
    'db_name':os.getenv("DB_NAME"),
    'user':os.getenv("DB_USER"),
    'pass':os.getenv("PASSWORD")
     }
)
#Interface de execucao do banco
DB_INTERFACE = DBConnect(DB_CONFIG)

"""
Sessao do Bot
"""
TELEGRAM_TOKEN = os.getenv("TELEGRAMBOT_KEY")
