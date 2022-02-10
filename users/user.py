from uuid import uuid1
from passlib.context import CryptContext


class User:
    def __init__(self, user_name, password, premium=False):
        self.id = str(uuid1())
        self.is_premium = premium
        self.user_name = user_name
        self.password = password
        self.playlist = {str: list}

    def add_song_to_playlist(self, song_name, playlist_name):
        if self.is_premium:
            self.playlist[playlist_name].append(song_name)
            return True
        else:
            if len(self.playlist[playlist_name]) != 20:
                self.playlist[playlist_name] = []
            else:
                return False

    def create_playlist(self, playlist_name):
        if self.is_premium:
            self.playlist[playlist_name] = []
            return True
        else:
            if len(self.playlist) != 5:
                self.playlist[playlist_name] = []
            else:
                return False

    def verify_user(self, password, user_name, context):
        return True if user_name == self.user_name and context.verify(password) else False
