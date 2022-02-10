from users.user import User


class Artist(User):
    def __init__(self, user_name, password):
        super().__init__(user_name, password)
        self.is_premium = True

    def get_artist_id(self):
        pass
