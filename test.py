# -*- coding: utf-8 -*-
_author_ = 'Pylar'
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(

      #EMAIL SETTINGS

     MAIL_SERVER='smtp.163.com',

     MAIL_PORT=465,

     MAIL_USE_SSL=True,

    MAIL_USERNAME = 'wxmy419@163.com',

     MAIL_PASSWORD = 'a123456' )




mail = Mail(app)

@app.route("/")

def index():

     msg = Message(subject="helloworld", sender='wxmy419@163.com', recipients=['1483287009@qq.com'])

     msg.html = "testinghtml"

     mail.send(msg)


if __name__ =='__main__':

    app.run(debug=True)