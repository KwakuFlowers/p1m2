from json import load
import os
from urllib import response
import requests
import json
import base64
import string
import random
import flask
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

GetReqURL = "https://api.spotify.com/v1"
api_token_url = "https://accounts.spotify.com/api/token"


def artistsongs(artid):
    Art_song_url = f"{GetReqURL}/artists/{artid}/top-tracks"
    Art_url = f"{GetReqURL}/artists/{artid}"
    country = {"country": "US"}

    head = {
        "Authorization": f"Bearer {authorize()}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    randomsong = random.randint(0, 9)
    songs = requests.get(Art_song_url, params=country, headers=head)
    artistinfo = requests.get(Art_url, headers=head)
    songinfo = songs.json()
    artinfo = artistinfo.json()
    artistname = artinfo["name"]
    # print(artistname)
    # track genreal info search
    randsonginfo = songinfo["tracks"][randomsong]
    # print(randsonginfo)
    # print(
    #    "-----------------------------------------------------------------------------------"
    # )
    # track name
    randsonginfo_name = randsonginfo["name"]
    # print(randsonginfo_name)
    # print(
    #    "-----------------------------------------------------------------------------------"
    # )
    # track release date
    randsonginfo_releasedate = randsonginfo["album"]["release_date"]
    # print(randsonginfo_releasedate)
    # print(
    #   "-----------------------------------------------------------------------------------"
    # )
    # Track popularity (out of 100)
    randsonginfo_popularity = randsonginfo["popularity"]
    # print(randsonginfo_popularity)
    # print(
    #    "-----------------------------------------------------------------------------------"
    # )
    # url to artist
    randsonginfo_extern = randsonginfo["external_urls"]["spotify"]
    # print(randsonginfo_extern)
    # print(
    #    "-----------------------------------------------------------------------------------"
    # )
    # image grab
    randsonginfo_imageurl = randsonginfo["album"]["images"][0]["url"]
    randsonginfo_imageH = randsonginfo["album"]["images"][0]["height"]
    randsonginfo_imageW = randsonginfo["album"]["images"][0]["width"]
    # print(randsonginfo_imageurl)
    # print(randsonginfo_imageH)
    # print(randsonginfo_imageW)
    # print(
    #    "-----------------------------------------------------------------------------------"
    # )
    return (
        randsonginfo_name,
        randsonginfo_releasedate,
        randsonginfo_popularity,
        randsonginfo_extern,
        randsonginfo_imageurl,
        randsonginfo_imageH,
        randsonginfo_imageW,
        artistname,
    )


def authorize():
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    DATA = {
        "Content-Type": "application/x-www-form-urlencoded",
        "grant_type": "client_credentials",
    }

    authkeydata = requests.post(
        api_token_url, auth=(CLIENT_ID, CLIENT_SECRET), data=DATA
    )
    reqkey = authkeydata.json()
    token = reqkey.get("access_token")
    # print(token)
    return f"{token}"


# artistsongs("3TVXtAsR1Inumwj472S9r4")  # used for testing in earlier implementations
