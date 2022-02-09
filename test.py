import fs.copy
from fs.memoryfs import MemoryFS
from fs.osfs import OSFS
from songs import songs_handler


def main():
    pass
    # mem_fs = MemoryFS()
    # drv_fs = OSFS("~liran/Documents/songs")
    # fs.copy.copy_fs(drv_fs, mem_fs)
    # print(mem_fs.listdir('.'))


if __name__ == '__main__':
    main()
