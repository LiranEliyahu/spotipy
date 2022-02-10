from heapq import nlargest


def find_all_artists(songs_list):
    artist_list = set()
    for song in songs_list:
        artist_list.add(song["track"]["artists"][0]["name"])
    return artist_list


def get_artist_songs(songs_list, artist_name):
    artist_songs = []
    for song in songs_list:
        if song["track"]["artists"][0]["name"] == artist_name:
            artist_songs.append([song["track"]["name"], song["track"]["popularity"]])
    return artist_songs


def get_top_ten(songs_list, artist):
    get_artist_songs(songs_list, artist)
    return nlargest(10, list(get_artist_songs(songs_list, artist)), key=lambda x: x[1])


def get_album_songs(album_name, songs_list):
    album = []
    for song in songs_list:
        if song["track"]["album"]["name"] == album_name:
            album.append([song["track"]["name"],  song["track"]["popularity"]])
    return album


def get_artist_album(songs_list, artist_name):
    albums = []
    for song in songs_list:
        if song["track"]["artists"][0]["name"] == artist_name:
            albums.append(song["track"]["album"]["name"])
    return albums
