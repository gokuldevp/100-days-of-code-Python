import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# ****************************** getting top 100 songs name from Billboard *********************************************

date = input("What year do you want to travel to? Enter the date in the format YYYY-MM-DD : ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

with requests.get(url=URL) as response:
    data = response.text

soup = BeautifulSoup(data, "html.parser")
top_100_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
top_100_songs_titles = [song.string for song in top_100_songs]

# ************************ creating a playlist in spotify of songs from billboard top 100 ******************************

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URL = "http://example.com"
SCOPE = "playlist-modify-private"
CACHE_PATH = "token.txt"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope=SCOPE,
                                               cache_path=CACHE_PATH,
                                               show_dialog=True))
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in top_100_songs_titles:
    result = sp.search(q=f"track:{song} year:{year}")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} is not in the spotify. Skipped")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
