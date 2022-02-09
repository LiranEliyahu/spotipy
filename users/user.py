from uuid import uuid1


class User:
    def __init__(self, user_name, password):
        self.user_id = str(uuid1())
        self.is_premium = bool
        self.user_name = str
        self.password = str
        self.playlist = {str: list}

    def add_song_to_playlist(self):
        pass
