from database import DB
import flask
import os


class User(DB.Model):
    id = DB.Culumn(DB.Integer, primary_key=True)
    Username = DB.Column(DB.string(256), is_nullable=False)
    email = DB.Column(DB.String(256), unique=True)
    password = DB.Column(DB.String(256), unique=True, is_nullable=False)


class Song_review(DB.Model):
    id = DB.Culumn(DB.Integer, primary_key=True)
    Username = DB.Column(DB.string(256), is_nullable=False)
    Song = DB.Column(DB.Integer, is_nullable=False)
    songrate = DB.Column(DB.Integer, is_nullable=False)
    songcomments = DB.Column(DB.string(256), is_nullable=False)


# DB.create_all()
