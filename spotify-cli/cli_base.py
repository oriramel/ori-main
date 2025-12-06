import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def main():
    # Set up authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
        redirect_uri='http://localhost:8888/callback',
        scope='user-read-recently-played'
    ))
    
    # Fetch recently played tracks
    results = sp.current_user_recently_played(limit=10)
    
    print("\n🎵 Your 10 Most Recently Played Songs:\n")
    print("-" * 60)
    
    for idx, item in enumerate(results['items'], 1):
        track = item['track']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        print(f"{idx}. {track['name']}")
        print(f"   Artist(s): {artists}")
        print(f"   Album: {track['album']['name']}")
        print()

if __name__ == '__main__':
    main()