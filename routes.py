import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
	# DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.mail.yahoo.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME"),
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	)
mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=["POST"])
def send_mail():
    try:
        msg = Message(request.form['subject'],
          sender="tamaramitryakova@yahoo.com",
          recipients=["tamaramitryakova@yahoo.com"])
        msg.body = request.form['email'] + " " + request.form['message']
        mail.send(msg)
        return render_template('home.html')

    except Exception, e:
        return(str(e))

if __name__ == '__main__':
    port = os.environ.get("PORT") or 5000
    app.run("0.0.0.0", port)
