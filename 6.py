import random

class Playlist:
    def __init__(self):
        self.songs = []

    def shuffle(self):
        random.shuffle(self.songs)

playlist = Playlist()

playlist.songs.append({'title': 'Song 1', 'artist': 'Artist A'})
playlist.songs.append({'title': 'Song 2', 'artist': 'Artist B'})
playlist.songs.append({'title': 'Song 3', 'artist': 'Artist C'})
playlist.songs.append({'title': 'Song 4', 'artist': 'Artist D'})
playlist.songs.append({'title': 'Song 5', 'artist': 'Artist E'})

playlist.shuffle()

for song in playlist.songs:
    print(f"Title: {song['title']}, Artist: {song['artist']}")
