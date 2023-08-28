from . import db
from flask_login import UserMixin
from sqlalchemy import LargeBinary


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    model = db.relationship('Model')