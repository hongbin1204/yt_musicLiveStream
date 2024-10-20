from queue import Queue
import threading

# music queue
q = Queue()

# path where music are stored, played when music queue is empty
STORED_PATH = "/Users/hb/Documents/music"

# path where music are downloaded
DOWNLOAD_PATH = "/Users/hb/Documents/downloads"

# array of recognized user
SAVED_USERS = ["Beans"]

# video id of the livestream
VIDEO_ID = "0_c0lH28tEg"