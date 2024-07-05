from spotipy.oauth2 import SpotifyClientCredentials
from pandas import read_csv
import spotipy
import pprint

keys = read_csv("keys.csv",index_col="names")
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=keys.at["client_id","info"],
                                                                         client_secret=keys.at["client_secret","info"]))

def artist_search(artist="Kid Cudi",sp=sp):
    result = sp.search('artist:' + artist,type="artist")
    items = result['artists']['items']
    if len(items) > 0:
        artist_object = items[0]
    return artist_object

def song_search(song="What Makes You Beautiful",sp=sp):
    result = sp.search('song:' + song,type="song")
    items = result['songs']['items']
    if len(items) > 0:
        song_object = items[0]
    return song_object