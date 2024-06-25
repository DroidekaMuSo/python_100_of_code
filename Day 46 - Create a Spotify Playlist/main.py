import requests
from bs4 import BeautifulSoup
from songs_manager import SongManager

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
song_manager = SongManager()

date = input("Which year do you want to travel to? \nType the date in this format YYYY-MM-DD:")

response = requests.get(url=f"{BILLBOARD_URL}/{date}")
billboard_data = response.text

soup = BeautifulSoup(billboard_data, "html.parser")

song_titles = soup.select(selector="li ul li h3")

songs = [song.getText().strip() for song in song_titles]
songs_uri = song_manager.getting_songs_uris(songs, date[:4])

song_manager.create_private_list(date, songs_uris=songs_uri)



