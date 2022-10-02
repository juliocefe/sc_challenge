from flask import Flask, render_template
from app.transactions import process_transactions
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
mail = Mail(app)

@app.route("/")
def hello_world():
    context = process_transactions()
    msg = Message("Holis", recipients=os.environ.get("RECIPIENTS").split(","))
    msg.html = render_template("email.html", context=context)
    mail.send(msg)
    return "Email has ben sent!"