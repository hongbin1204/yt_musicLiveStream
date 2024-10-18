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

# threading event use to stop a current running play_audio thread 
STOP_EVENT = threading.Event()

# video id of the livestream
VIDEO_ID = "1OLiFLlGTq0"