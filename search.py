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

def song_search(song="the other side of the door",artist="NA",sp=sp):
    p = 'track:' + song
    if artist != "NA":
        p = 'artist:' + artist + ' ' + p
    result = sp.search(q=p ,type="track")
    items = result['tracks']['items']
    if len(items) > 0:
        song_object = items[0]
    return song_object

def album_search(album="Rumours",artist="NA",sp=sp):
    p = 'album:' + album
    if artist != "NA":
        p = p + ' artist:' + artist 
    result = sp.search(q=p ,type="album")
    items = result['albums']['items']
    if len(items) > 0:
        album_object = items[0]
    return album_object

def get_artist_uri(artist="Kid Cudi",sp=sp):
    artist_object = artist_search(artist=artist,sp=sp)
    return artist_object["uri"]


def get_song_uri(song="the other side of the door",artist="NA",sp=sp):
    song_object = song_search(song=song,artist=artist)
    return song_object["uri"]

def get_album_uri(album="Rumours",artist="NA",sp=sp):
    album_object = album_search(album=album,artist=artist)
    return album_object["uri"]


def get_artist_albums(artist="Kid Cudi",sp=sp):
    results = sp.artist_albums(get_artist_uri(artist), album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    return albums