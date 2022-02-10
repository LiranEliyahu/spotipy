from heapq import nlargest


def find_all_artists(songs_list):
    artist_list = set()
    for song in songs_list:
        artist_list.add(song["track"]["artists"][0]["name"])
    print(*artist_list)
    return artist_list


def get_artist_songs(songs_list):
    artist_name = input("enter artist name: ")
    artist_songs = []
    for song in songs_list:
        if song["track"]["artists"][0]["name"] == artist_name:
            artist_songs.append([song["track"]["name"], song["track"]["popularity"]])
    print(*artist_songs)
    return artist_songs


def get_top_ten(songs_list):
    nlargest(10, list(get_artist_songs(songs_list)), key=lambda x: x[1])


def get_album_songs(songs_list):
    album_name = input("enter album name: ")
    album = []
    for song in songs_list:
        if song["track"]["album"]["name"] == album_name:
            album.append([song["track"]["name"],  song["track"]["popularity"]])
    print(*album)


def get_artist_album(songs_list):
    artist_name = input("enter artist name: ")
    albums = []
    for song in songs_list:
        if song["track"]["artists"][0]["name"] == artist_name:
            albums.append(song["track"]["album"]["name"])
    print(*albums)
