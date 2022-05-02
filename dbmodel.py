from app import DB, LoginManager
import flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    login_required,
    UserMixin,
)


class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    Username = DB.Column(DB.String(256))
    Email = DB.Column(DB.String(256), unique=True)
    Password = DB.Column(DB.String(256), unique=True)

    def get_id(self):
        return self.Email

    def is_active(self):
        return True


class Song_review(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    Username = DB.Column(DB.String(256))
    Art_name = DB.Column(DB.String(256))
    Song = DB.Column(DB.String(50))
    songrate = DB.Column(DB.Integer)
    songcomments = DB.Column(DB.String(256))


DB.create_all()  # uncomment when ready to push columns to database
