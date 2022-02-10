from songs import songs_handler
from search import search


def main():
    songs = songs_handler.merge_songs_files()

    print(songs)
    print(search.find_all_artists(songs))
    print(search.get_artist_songs(songs, "Margalit Tzan'ani"))
    print(search.get_top_ten(songs, "Margalit Tzan'ani"))
    print(search.get_album_songs("Bringing It All Back Home", songs))
    print(search.get_artist_album(songs, "Margalit Tzan'ani"))


if __name__ == '__main__':
    main()
