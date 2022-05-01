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
geniusapi = "http://api.genius.com"
# songname = "Sing About Me Im Dying Of Thirst"


def songlyrics(songname):
    new_songname = songname.replace(" ", "%20")
    song_lyrics_results = f"{geniusapi}/search?q=/{new_songname}"
    # print(new_songname)
    token = os.getenv("GACCESS_TOKEN")
    head = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    result = requests.get(song_lyrics_results, headers=head)
    result_info = result.json()
    firsturl = result_info["response"]["hits"][0]["result"]["url"]
    # print(firsturl)
    return f"{firsturl}"


# songlyrics(songname)
