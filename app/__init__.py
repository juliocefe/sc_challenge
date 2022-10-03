from flask import Flask, render_template
from app.transactions import process_transactions
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER", "mailhog")
app.config["MAIL_PORT"] = int(os.environ.get("MAIL_PORT", 1025))
app.config["MAIL_USE_SSL"] = (os.environ.get("MAIL_USE_SSL", "False")) == "True"
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME", "mailhog")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD", "mailhog")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER", "test@mailhog.local")
mail = Mail(app)

@app.route("/")
def hello_world():
    context = process_transactions()
    recipients = os.environ.get(
        "RECIPIENTS", 
        "customer@mailserver.domain"
    ).split(",")
    msg = Message("Holis", recipients=recipients)
    msg.html = render_template("email.html", context=context)
    mail.send(msg)
    return "Email has ben sent!"