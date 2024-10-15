import flask
import flask_mail
from main.mail_config import mail
def render_home():
    if flask.request.method == "POST":
        try:
            msg = flask_mail.Message(
                subject = 'Hello',
                recipients=['daria.filinskaya2009@gmail.com'],
                body='This is a test email sent from Flask-Mail!'
            )
            mail.send(msg)
            print("home views")
        except:
            print("home views error")
    return flask.render_template("home.html")