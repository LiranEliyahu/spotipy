import os
import json
from functools import lru_cache, wraps
from datetime import datetime, timedelta


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)
        return wrapped_func
    return wrapper_cache


@timed_lru_cache(600, maxsize=1)
def merge_songs_files(songs_path='C:\\Users\\liran\\Documents\\giTasks\\spotipy\\resources\\songs\\'):
    song_list = [json.load(open(songs_path + file, "r")) for file in os.listdir(songs_path)]
    return song_list
