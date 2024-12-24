import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyClient:
    def __init__(self, travel_date, songs, client_id, client_secret, username):
        self.travel_date = travel_date
        self.songs = songs
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username

        self.spotify = None
        self.user_id = None
        self.playlist_id = None
        self.song_uris = []
        self.authenticate()
    def authenticate(self):
        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri="http://localhost:8888/callback",
                scope="playlist-modify-private",
                cache_path="token.txt",
                username=self.username,
                requests_timeout=5,
                show_dialog=True,
            )
        )
        self.user_id = self.spotify.current_user()["id"]
        print(f"Authenticated for user: {self.user_id}")
    def get_uris(self):
        year = self.travel_date.split("-")[0]
        for song in self.songs:
            query = f"track:{song} year:{year}"
            print(f"Searching for: {query}")

            result = self.spotify.search(q=query, type="track", limit=1)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
                print(f"Song name {song}")
                print(f"Found URI for '{song}': {uri}")
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
    def create_playlist(self):
        playlist_name = f"{self.travel_date} Billboard 100"
        print(f"Creating playlist: '{playlist_name}'")

        playlist = self.spotify.user_playlist_create(
            user=self.user_id,
            name=playlist_name,
            public=False,
            collaborative=False,
        )
        self.playlist_id = playlist['id']
        print(f"Created playlist with ID: {self.playlist_id}")
    def add_songs_to_playlist(self):
        if not self.playlist_id:
            raise ValueError("Playlist has not been created. Call create_playlist() first.")
        total_songs = len(self.song_uris)
        print(f"Adding {total_songs} songs to playlist (ID: {self.playlist_id})...")
        if total_songs == 0:
            print("No song URIs to add.")
            return
        is_done = 0
        for song_uri in self.song_uris:
            is_done += 1
            self.spotify.playlist_add_items(playlist_id=self.playlist_id, items=[song_uri])
            print(f"From 100/{is_done} is done")
        print(f"All {total_songs} songs have been added to your '{self.travel_date} Billboard 100' playlist.")