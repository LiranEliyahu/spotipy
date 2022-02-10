from songs import songs_handler
from search import search
from menu.menu import sign_user_up, login_user


def main():
    songs = songs_handler.merge_songs_files()

    print(songs)
    print(search.find_all_artists(songs))
    print(search.get_artist_songs(songs, "Margalit Tzan'ani"))
    print(search.get_top_ten(songs, "Margalit Tzan'ani"))
    print(search.get_album_songs("Bringing It All Back Home", songs))
    print(search.get_artist_album(songs, "Margalit Tzan'ani"))
    # sign_user_up()
    print(login_user())


if __name__ == '__main__':
    main()
