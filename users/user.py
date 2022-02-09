from uuid import uuid1


class User:
    def __init__(self, user_name, password):
        self.user_id = str(uuid1())
        self.is_premium = bool
        self.user_name = str
        self.password = str
        self.playlist = {str: list}

    def add_song_to_playlist(self, song_name, playlist_name):
        if self.is_premium:
            self.playlist[playlist_name].append(song_name)
            print("added new song!")
        else:
            if len(self.playlist[playlist_name]) != 20:
                self.playlist[playlist_name] = []
            else:
                print("no can do, pay up!")

    def create_playlist(self, playlist_name):
        if self.is_premium:
            self.playlist[playlist_name] = []
            print("created a new playlist")
        else:
            if len(self.playlist) != 5:
                self.playlist[playlist_name] = []
            else:
                print("no can do, pay up!")
