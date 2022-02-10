from consolemenu import *
from consolemenu.items import *

from search.search import get_artist_songs, find_all_artists, get_top_ten, get_album_songs, get_artist_album
from songs.songs_handler import merge_songs_files

def check(n=1, n2=1):
    print(n == n2)


def main():
    # # Create the welcome_menu
    # welcome_menu = ConsoleMenu("Spotipy", "welcome to the best music app without music!")
    # login_menu = ConsoleMenu("login", "login to enjoy tons of song titles")
    # sign_up_menu = ConsoleMenu("sign up", "sign up to enjoy tons of song titles")
    # artist_menu = ConsoleMenu("sign up", "sign up to enjoy tons of song titles")
    # main_menu = ConsoleMenu("hello", "welcome to the best music app without music!")
    # search_manu = ConsoleMenu("search", "come on, try something")
    #
    # # A FunctionItem runs a Python function when selected
    # function_item = FunctionItem("test", check())
    #
    # # A SelectionMenu constructs a welcome_menu from a list of strings
    # selection_menu = SelectionMenu(["user name", "password", "artist"])
    #
    # # A SubmenuItem lets you add a welcome_menu (the selection_menu above, for example)
    # # as a submenu of another welcome_menu
    #
    # test = SubmenuItem("search", search_manu, menu=login_menu)
    # # print(test)
    # login_menu.append_item(test)
    #
    # login = SubmenuItem("login", login_menu, menu=welcome_menu)
    # sign_up = SubmenuItem("sign up", sign_up_menu, menu=welcome_menu)
    # artist_login = SubmenuItem("artist", artist_menu, menu=welcome_menu)
    #
    # # Once we're done creating them, we just add the items to the welcome_menu
    # welcome_menu.append_item(function_item)
    # welcome_menu.append_item(login)
    # welcome_menu.append_item(sign_up)
    # welcome_menu.append_item(artist_login)
    #
    # # Finally, we call show to show the welcome_menu and allow the user to interact
    # welcome_menu.show()
    # welcome_menu.exit()

    # Import the necessary packages

    # Create the menu
    menu = ConsoleMenu("Title", "Subtitle")
    welcome_menu = ConsoleMenu("Spotipy", "welcome to the best music app without music!")
    login_menu = ConsoleMenu("login", "login to enjoy tons of song titles")
    sign_up_menu = ConsoleMenu("sign up", "sign up to enjoy tons of song titles")
    artist_menu = ConsoleMenu("sign up", "sign up to enjoy tons of song titles")
    main_menu = ConsoleMenu("hey bro", "welcome to the best music app without music!")
    search_manu = ConsoleMenu("search", "come on, try something")

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    menu_item = MenuItem("Menu Item")

    # A FunctionItem runs a Python function when selected
    function_item = FunctionItem("Call a Python function", check, ["Enter an input"])

    # A CommandItem runs a console command
    command_item = CommandItem("Run a console command", "touch hello.txt")

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

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(["item1", "item2", "item3"])

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(menu_item)
    menu.append_item(function_item)
    menu.append_item(command_item)
    menu.append_item(submenu_item)

    login = SubmenuItem("login", login_menu, menu=welcome_menu)
    sign_up = SubmenuItem("sign up", sign_up_menu, menu=welcome_menu)
    artist_login = SubmenuItem("artist", artist_menu, menu=welcome_menu)

    welcome_menu.append_item(login)
    welcome_menu.append_item(sign_up)
    welcome_menu.append_item(artist_login)

    # Finally, we call show to show the menu and allow the user to interact
    welcome_menu.show()


if __name__ == '__main__':
    main()
