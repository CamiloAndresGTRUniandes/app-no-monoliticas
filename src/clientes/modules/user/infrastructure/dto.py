
from config.db import db


Base = db.declarative_base()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    fisrtName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    userName = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    