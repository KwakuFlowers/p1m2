import flask
from flask import Flask, render_template, redirect, session, url_for, request, flash
import random

from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool, NullPool
from sqlalchemy.orm import sessionmaker

from dbmodel import *
import os
from Genius import songlyrics
from Spot import artistsongs

app = flask.Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    login_required,
    UserMixin,
    logout_user,
)

login_manager = LoginManager()
userinfourl = os.getenv("USERDATA_URL")

if userinfourl.startswith("postgres://"):
    userinfourl = userinfourl.replace("postgres://", "postgresql://", 1)
    # print(userinfourl)
app.config["SQLALCHEMY_DATABASE_URI"] = userinfourl
# app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
#    "pool_size": 20,
#    "pool_recycle": 10,
#    "pool_pre_ping": True,
# }
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "secret key"

# engine = create_engine(
#    userinfourl, poolclass=NullPool  # uncomment for other push to git
# )
#
# Session = sessionmaker(engine)


# @app.teardown_appcontext
# def shutdown_session(exception=None):
# DB.session.remove()


# Everything in comments above are my attempts to create an engine through the app in order for the app to
# constinously  add data to database without getting an error for too many connections to database.

DB = SQLAlchemy(app)

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(Email=user_id).first()


login_manager.login_view = "login"


@app.route("/")
def main():
    return redirect("signup")
    # used for base place where user goes


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "GET":
        return flask.render_template("signup.html")
    userinfo = flask.request.form
    Username2 = userinfo["Username2"]
    Password2 = userinfo["Password2"]
    Email2 = userinfo["Email2"]

    found = User.query.filter_by(Email=Email2).first()

    if found != None:
        flash("User already exists with that email")
        return flask.render_template("signup.html")
    else:
        adduser = User(Username=Username2, Password=Password2, Email=Email2)
        DB.session.add(adduser)
        DB.session.commit()
        return redirect("login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("login.html")

    userinfo = flask.request.form
    Username2 = userinfo["Username2"]
    Password2 = userinfo["Password2"]
    Email2 = userinfo["Email2"]

    found = User.query.filter_by(
        Username=Username2, Password=Password2, Email=Email2
    ).first()

    if found == None:
        flash("You aren't registered! Return to signup!")
        return flask.render_template("login.html")
    else:
        login_user(found)
        return redirect("rand")


@app.route("/new_review", methods=["POST"])
def new_review():
    rev = flask.request.form
    rating = rev.get("rating")
    artist = rev.get("artist")
    review = rev.get("review")
    Song = rev.get("song")
    # art_name = rev.get("artname")

    cur = Song_review(  # exactly the same as adding a new user to DB
        Username=current_user.Username,
        songrate=rating,
        songcomments=review,
        Song=Song,
        Art_name=artist,  # possible implementation to seperate reviews if artists have the same named song
    )
    DB.session.add(cur)
    DB.session.commit()
    DB.session.close()
    return redirect("rand")


@app.route("/rand")
def rand():
    artistid = [
        "3TVXtAsR1Inumwj472S9r4",  # Drake
        # "5f7VJjfbwm532GiveGC0ZK",  # Lil Baby
        # "6vWDO969PvNqNYHIOW5v0m",  # Beyonce
        # "2hlmm7s2ICUX0LVIhVFlZQ",  # Gunna
        # "6l3HvQ5sa6mXTsMTB19rO5",  # J. cole
        # "2YZyLoL8N0Wb9xBt1NhZWg",  # Kendrick Lamar
    ]
    newartisitid = random.choice(artistid)
    (
        randsonginfo_name,
        randsonginfo_releasedate,
        randsonginfo_popularity,
        randsonginfo_extern,
        randsonginfo_imageurl,
        randsonginfo_imageH,
        randsonginfo_imageW,
        artistname,
    ) = artistsongs(newartisitid)
    currsongname = randsonginfo_name
    geniuslink = songlyrics(currsongname)
    # print(currsongname)
    # Art_name = newartisitid#
    review = Song_review.query.filter_by(Song=currsongname, Art_name=artistname).all()
    # print(review) tests why Song reviews weren't saving and how to implement them to webpage

    return flask.render_template(
        "start.html",
        songname=randsonginfo_name,
        popularity=randsonginfo_popularity,
        spotlink=randsonginfo_extern,
        releasedate=randsonginfo_releasedate,
        imageurl=randsonginfo_imageurl,
        imageheight=randsonginfo_imageH,
        imagewidth=randsonginfo_imageW,
        genlink=geniuslink,
        Song=currsongname,
        reviewed=review,
        artistname=artistname,
    )
    # possibly move everything from main into here and have login
    # be first thing User does on app


@app.route("/logout")
def logout():
    logout_user()
    return redirect("login")


if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 8080)) #uncomment when pushing to heroku and no local testing
    app.run()  # host="0.0.0.0", port=port)

# app.run(
#    host=os.getenv("IP", "0.0.0.0"), port=port, debug=False #uncomment when sending to heroku
# )

# os.getenv("PORT", 5000)
