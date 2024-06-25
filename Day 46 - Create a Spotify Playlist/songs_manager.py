import time

import dotenv
import os

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

dotenv.load_dotenv()


class SongManager:
    def __init__(self):
        self.sp = None
        self.CLIENT_ID = os.environ.get("CLIENT_ID")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        self.ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

        self.user_id = self.getting_user_id()

    def getting_user_id(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.CLIENT_ID,
                client_secret=self.CLIENT_SECRET,
                redirect_uri="http://example.com",
                scope="playlist-modify-private",
                show_dialog=True,
                cache_path="token.txt",
                username="Diego Muñoz"
            )
        )

        user_id = self.sp.current_user()["id"]
        return user_id

    def getting_songs_uris(self, song_list, year):
        songs_uri = []

        for song in song_list:
            track = self.sp.search(q=f"track:{song} year:{year}", type="track", limit=1, market="US")
            try:
                uri = track["tracks"]["items"][0]["uri"]
                songs_uri.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

        return songs_uri

    def create_private_list(self, date, songs_uris):
        playlist = self.sp.user_playlist_create(user=self.user_id, name=date, public=False)

        self.sp.playlist_add_items(playlist_id=playlist['id'], items=songs_uris)

        print(f"This is the link to your playlist {playlist['external_urls']['spotify']}, Enjoy it!")





song_manager = SongManager()
