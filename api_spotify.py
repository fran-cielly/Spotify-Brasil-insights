# %%
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def spotipy_api():
    client_id = os.getenv("SPOTIPY_CLIENT_ID ")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
    )
    return sp
  
def find_all_artists():
    sp = spotipy_api()
    all_artists = []
    char = "abcdefghijklmnopqrstuvwxyz0123456789"

    for letter in char:
        offset = 0
        while True:
            result = sp.search(q=letter, type="artist", limit=50, offset=offset)
            artists = result["artists"]["items"]

            if not artists:
                break

            for artist in artists:
                all_artists.append(artist)

            offset += 50
            if offset >= result["artists"]["total"]:
                break

    return all_artists

def find_artists_by_genre(genre, lista):
    artists_by_genre = [
        artist for artist in lista()
            if genre in artist['genres']
    ]
    return artists_by_genre