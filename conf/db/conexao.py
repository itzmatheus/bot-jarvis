import psycopg2

'''
Arquivo contendo as configurações e conexões do BANCO
PostgreSQL 10
pgAdmin 4
'''

class Conexao(object):

    def __init__(self, host: object, port: object, db_name: object, db_user: object, db_pass: object) -> object:
        try:
            self._db = psycopg2.connect(host=host,port=port, database=db_name, user=db_user,  password=db_pass)
            self.cursor = self._db.cursor()
            print("Conectado: {host}:{port}/{db}. User: {usuario}.".format(host=host,db=db_name,port=port,usuario=db_user))
        except ValueError as e:
            print(e)

    #Metodo para fechar conexao do objeto com banco
    def close(self):
        self.cursor.close()
        print("Conexão fechada!")

