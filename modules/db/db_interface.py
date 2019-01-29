from modules.db.conexao import Conexao


class DBConnect(object):

    def __init__(self, DB_CONFIG : object):
        self._connection = Conexao(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            db_name=DB_CONFIG['db_name'],
            db_user=DB_CONFIG['user'],
            db_pass=DB_CONFIG['pass']
        )
        self._cursor = self._connection.cursor

    def select(self, sql, type=None):
        '''
        :param sql: SQL Query
        :param type: Tipo de retorno dos dados
        :return: Retorna o resultado da query
        '''
        _data = None
        try:
            self._cursor.execute(sql)
            data = self._cursor
        except ValueError as e:
            return e

        if type == dict:
            _data = self._dictfetchall(self._cursor)
        else:
            _data = self._cursor.fetchall()

        self._cursor.close()
        return _data


    def insert(self, sql, commit=False):
        """
        :param sql: SQL Query
        :param commit: Realizar commit transacional
        :return: True se for inserido, se houver algum erro retorna o erro
        """
        try:
            self._cursor.execute(sql)
            if commit:
                self._cursor.commit()

            self._cursor.close()
            return True
        except ValueError as e:

            self._cursor.close()
            return e

    '''
    Metodo para retornar dados no formato de dicionario
    '''
    def _dictfetchall(self, cursor):
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]