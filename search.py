from spotipy.oauth2 import SpotifyClientCredentials
from pandas import read_csv
import spotipy
import sys
import pprint

keys = read_csv("keys.csv",index_col="names")

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Kid Cudi'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=keys.at["client_id","info"],
                                                                         client_secret=keys.at["client_secret","info"]))
result = sp.search('artist:' + search_str,type="artist")
items = result['artists']['items']
if len(items) > 0:
    artist = items[0]
    pprint.pprint(artist)