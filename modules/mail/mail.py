import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from projeto.core.settings import EMAIL_CONFIG


class Mail(object):
    _server: SMTP

    def __init__(self, EMAIL_CONFIG: object):
        self._server = self.connect(
            email=EMAIL_CONFIG['email'], password=EMAIL_CONFIG['password'],
            server=EMAIL_CONFIG['smtp'], port=EMAIL_CONFIG['port'])
        self._from = EMAIL_CONFIG['email']

    def connect(self, email, password, server, port):
        self._server = smtplib.SMTP(server, port)
        self._server.starttls()
        self._server.login(email, password)
        print("Servidor conectado {server}:{port}. Email {email}".format(
            server=server, port=port, email=email))
        return self._server

    def close(self):
        self._server.quit()
        print("Conexão com serviço de email fechada!")

    def send_mail(self, _mail_to, _title, _message, _filepath=None):
        _msg = MIMEMultipart()

        _msg['From'] = self._from
        _msg['To'] = _mail_to
        _msg['Subject'] = _title
        _body = _message

        _msg.attach(MIMEText(_body, 'plain'))

        # Anexando arquivo caso exista ao corpo do email
        if _filepath:
            _attachment = open(_filepath, 'rb')
            _part = MIMEBase('application', 'octet-stream')
            _part.set_payload(_attachment.read())
            encoders.encode_base64(_part)
            _part.add_header('Content-Disposition', "attachment; filename= %s " % _filepath)
            _msg.attach(_part)
            _attachment.close()

        self._server.sendmail(self._from, _mail_to, _msg.as_string())
        print('''== Email enviado ==
{email}
            '''.format(email=_msg))