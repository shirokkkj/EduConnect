from config_app import db
import datetime

class Schools(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    name = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    adress = db.Column(db.String(200), unique=True, nullable=False)
    telephone = db.Column(db.String(200), unique=True, nullable=False)