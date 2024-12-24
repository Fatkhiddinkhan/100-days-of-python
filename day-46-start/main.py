from music_date import MusicData
from spotify import SpotifyClient
import os

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
USERNAME = os.environ.get("USERNAME")


tries = 0
while tries < 3:
    user_prompt = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD: ")
    songs_list = MusicData(user_prompt)

    if songs_list.billboard_response and songs_list.songs:
        print("Songs fetched successfully!")
        spotify_client = SpotifyClient(
            travel_date=user_prompt,
            songs=songs_list.songs,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            username=USERNAME,
        )
        # Search for URIs of these songs on Spotify
        spotify_client.get_uris()

        # Create a new playlist
        spotify_client.create_playlist()

        # Add found songs to the playlist
        spotify_client.add_songs_to_playlist()

        # Break out of the loop after success
        break
    else:
        tries += 1
        print("Try again.")
else:
    print("Sorry, too many attempts. Please try again later.")


