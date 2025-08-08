import pandas as pd
import json

from api_spotify import find_artists_by_genre, find_all_artists

all_artists = find_all_artists()

for artista in all_artists:
    print(artista)