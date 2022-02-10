from uuid import uuid1


class User:
    def __init__(self, user_name, password, premium=False):
        self.id = str(uuid1())
        self.is_premium = premium
        self.user_name = user_name
        self.password = password
        self.playlist = {}

    def add_song_to_playlist(self, song_name):
        playlist_name = input("enter playlist name: ")
        if self.is_premium:
            self.playlist[playlist_name].append(song_name)
            print("added new song!")
        else:
            if len(self.playlist[playlist_name]) != 20:
                self.playlist[playlist_name] = []
                print("added new song!")
            else:
                print("pay up")

    def create_playlist(self):
        playlist_name = input("enter playlist name: ")
        if self.is_premium:
            self.playlist[playlist_name] = []
            print("added new playlist!")
        else:
            if len(self.playlist) != 5:
                self.playlist[playlist_name] = []
                print("added new playlist!")
            else:
                print("pay up")
