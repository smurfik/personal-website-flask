from flask import Flask, render_template
from flask_mail import Mail, Message
import config

app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.mail.yahoo.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = config.MAIL_USERNAME,
	MAIL_PASSWORD = config.MAIL_PASSWORD
	)
mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mail')
def send_mail():
    try:
        msg = Message("Send Mail!",
          sender="tamaramitryakova@yahoo.com",
          recipients=["tamaramitryakova@yahoo.com"])
        msg.body = "Yo!\nHave you heard the good word of Python???"
        mail.send(msg)
        return 'Mail sent!'

    except Exception, e:
        return(str(e))


if __name__ == '__main__':
    app.run()
