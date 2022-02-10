def find_all_artists(songs_list):
    artist_list = set()
    for song in songs_list:
        artist_list.add(song["artist"]["name"])
    return artist_list


def get_artist_songs(songs_list, artist_name):
    artist_songs = set()
    for song in songs_list:
        if song["artist"]["name"] == artist_name:
            artist_songs.add([song["name"], song["popularity"]])
    return artist_songs


def get_top_ten(songs_list, artist):
    get_artist_songs(songs_list, artist)
    return sorted(list(get_artist_songs(songs_list, artist)), key=lambda x: x[1], reverse=True)


def get_album_songs(album_name):
    pass
