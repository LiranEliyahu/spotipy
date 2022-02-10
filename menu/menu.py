import json
import logging
from passlib.context import CryptContext
from search.search import get_artist_songs, find_all_artists, get_top_ten, get_album_songs, get_artist_album
from songs.songs_handler import merge_songs_files
from users.user import User
from consolemenu import *
from consolemenu.items import *

context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)

logging.basicConfig(filename=
                    'C:\\Users\\liran\\Documents\\giTasks\\spotipy\\resources\\loggs\\info.log',
                    encoding='utf-8', level=logging.INFO)
logging.basicConfig(filename=
                    'C:\\Users\\liran\\Documents\\giTasks\\spotipy\\resources\\loggs\\error.log',
                    encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger('menu_loger')


def sign_user():
    password = input("enter password: ")
    user_name = input("enter user name: ")
    user = User(user_name, context.hash(password))
    add_user_data(user)
    return user


def add_artist_data(artist,
                    path="C:\\Users\\liran\\Documents\\giTasks\\spotipy\\resources\\userAndArtistData\\artist.json"):
    try:
        with open(path, 'r+') as file:
            artist_dict = {
                "_id": artist.id,
                "artist_name": artist.user_name,
                "password": artist.password,
                "playlist": artist.playlist
            }

            file_data = json.load(file)
            file_data["artist"].append(artist_dict)
            file.seek(0)
            json.dump(file_data, file, indent=4)
            logger.info('new artist added: ' + artist.user_name)
            return True
    except Exception as e:  # work on python 3.x
        logger.error('Failed to upload to ftp: ' + str(e))


def add_user_data(user,
                  path="C:\\Users\\liran\\Documents\\giTasks\\spotipy\\resources\\userAndArtistData\\users.json"):
    try:
        with open(path, 'r+') as file:
            user_dict = {
                "_id": user.id,
                "user_name": user.user_name,
                "password": user.password,
                "playlist": user.playlist
            }

            file_data = json.load(file)
            file_data["users"].append(user_dict)
            file.seek(0)
            json.dump(file_data, file, indent=4)
            logging.info('new user added: ' + user.user_name + " -> " + user.id)
            return True
    except Exception as e:  # work on python 3.x
        logger.error('Failed to upload to ftp: ' + str(e))


def login_user(path="C:\\Users\\liran\\Documents\\giTasks\\spotipy\\resources\\userAndArtistData\\users.json"):
    user_name = input("enter user name: ")
    password = input("enter password: ")
    try:
        with open(path, "r") as users_data:
            users = json.load(users_data)
            for user in users["users"]:
                if user_name in user["user_name"] and context.verify(password, user["password"]):
                    logger.info("user: " + user["_id"] + " logged in")
                    print("ok")
                    return True
                else:
                    logger.info("user: " + user["_id"] + " tried to get in but failed")
                    print("try again")
                    return False
    except Exception as e:  # work on python 3.x
        logger.error('Failed to upload to ftp: ' + str(e))


def menu_handler():
    # all the menus
    artist_menu = ConsoleMenu("sign up", "sign up to enjoy tons of song titles")
    main_menu = ConsoleMenu("Spotipy\nhey bro", "welcome to the best music app without music!")
    user_menu = ConsoleMenu("user controls", "add some, remove some it's your choice!")
    search_manu = ConsoleMenu("search", "come on, try something")


    # search menu
    artist_songs_func = FunctionItem("artists songs", get_artist_songs, [merge_songs_files()])
    all_artists_func = FunctionItem("all artists", find_all_artists, [merge_songs_files()])
    top_ten_func = FunctionItem("top 10 of an artist", get_top_ten, [merge_songs_files()])
    album_songs_func = FunctionItem("songs in album", get_album_songs, [merge_songs_files()])
    artist_album_func = FunctionItem("albums of artist", get_artist_album, [merge_songs_files()])
    search_manu.append_item(artist_songs_func)
    search_manu.append_item(all_artists_func)
    search_manu.append_item(top_ten_func)
    search_manu.append_item(album_songs_func)
    search_manu.append_item(artist_album_func)

    # user menu
    create_playlist = FunctionItem("create playlist", get_artist_songs, [merge_songs_files()])
    add_songs_to_playlist = FunctionItem("add songs to playlist", get_artist_songs)
    show_playlist = FunctionItem("show playlist", get_artist_songs)
    user_menu.append_item(create_playlist)
    user_menu.append_item(add_songs_to_playlist)
    user_menu.append_item(show_playlist)

    # all the submenus in welcome menu
    artist_login = SubmenuItem("artist", artist_menu, menu=welcome_menu)
    welcome_menu.append_item(artist_login)

    # all the submenus in main menu
    search_submenu = SubmenuItem("search", search_manu, menu=main_menu)
    user_submenu = SubmenuItem("user", user_menu, menu=main_menu)
    main_menu.append_item(search_submenu)
    main_menu.append_item(user_submenu)

    user_input = input("login or singup? you can exit")

    while user_input != "exit":
        if user_input == "login":
            if login_user():
                main_menu.show()
            else:
                print("try again")
        elif user_input == "signup":
            sign_user()

