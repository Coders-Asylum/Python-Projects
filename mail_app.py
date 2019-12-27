import os
import time

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['Email_user_id'],
    "MAIL_PASSWORD": os.environ['Email_password']
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    choice = 1
    print("Welcome to Python Mail\n"
          "* the mail sent would take few seconds to arrive at the receivers inbox, so be  patient............")
    while choice != 0:
        print("1) Send Mail\n2) exit")

        choice = int(input("Enter the no. of the choice: "))

        if choice == 1:
            mail_subject = input("Enter the subject: ")
            mail_recipient = input("Enter the Receivers address: ")
            mail_message = input("Enter the message: ")

            with app.app_context():
                start_time = time.time()
                msg = Message(subject=mail_subject,
                              sender=app.config.get("MAIL_USERNAME"),
                              recipients=[mail_recipient],
                              body=mail_message)
                mail.send(msg)
                end_time = time.time()
                print("Time taken to send message:\t", end_time - start_time)
        else:
            choice = 0
