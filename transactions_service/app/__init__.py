from flask import Flask, render_template
from app.transactions import TransactionsProcessor
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import os

app = Flask(__name__)
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = int(os.environ.get("MAIL_PORT"))
app.config["MAIL_USE_SSL"] = (os.environ.get("MAIL_USE_SSL", "False")) == "True"
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

mail = Mail(app)
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Transaction = Base.classes.accounts_transactions

def hello_world():
    processor = TransactionsProcessor(file_name="transactions.csv")
    msg = Message("Holis", recipients=os.environ.get("RECIPIENTS").split(","))
    msg.html = render_template("email.html", context=processor.data)
    mail.send(msg)
    return "Email has ben sent!"