from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv('.env')

class JukeBoxEmail:
    def _send_email(self, msg):
        with smtplib.SMTP_SSL(os.getenv('MAIL_SERVER'), port=os.getenv('MAIL_PORT')) as smtp:
          smtp.login(os.getenv('MAIL_USERNAME'), os.getenv('MAIL_PASSWORD'))
          smtp.send_message(msg)

    def message(self, subject, message_to, message_template, message_from=os.getenv('MAIL_USERNAME')):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = message_from
        msg["To"] = message_to
        msg.add_alternative(message_template, subtype="html")
        self._send_email(msg)


