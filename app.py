import flask
import random
from dbmodel import User
import os
from Genius import songlyrics
from Spot import artistsongs

app = flask.Flask(__name__)
from flask_login import LoginManager
login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/random")
def start():
    #possibly move everything from main into here and have login 
    #be first thing User does on app

@app.route("/")
def main():
    artistid = [
        "3TVXtAsR1Inumwj472S9r4",  # Drake
        "5f7VJjfbwm532GiveGC0ZK",  # Lil Baby
        "6vWDO969PvNqNYHIOW5v0m",  # Beyonce
        "2hlmm7s2ICUX0LVIhVFlZQ",  # Gunna
        "6l3HvQ5sa6mXTsMTB19rO5",  # J. cole
        "2YZyLoL8N0Wb9xBt1NhZWg",  # Kendrick Lamar
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
    ) = artistsongs(newartisitid)

    currsongname = randsonginfo_name
    geniuslink = songlyrics(currsongname)

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
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# app.run(
#    host=os.getenv("IP", "0.0.0.0"), port=port, debug=False #uncomment when sending to heroku
# )

# os.getenv("PORT", 5000)
