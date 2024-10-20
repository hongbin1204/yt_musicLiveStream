import pytchat
from time import sleep
from pytubefix import YouTube
import os, random, vlc, threading
from youtubesearchpython import VideosSearch
from config import DOWNLOAD_PATH, SAVED_USERS, STORED_PATH, VIDEO_ID, q

NEXT_SONG = False

def play_audio(file_path):
    global NEXT_SONG
    player = vlc.MediaPlayer(file_path)
    player.play()

    sleep(2)
    while player.is_playing():
        if NEXT_SONG:
            NEXT_SONG = False
            player.stop()
            break
        sleep(1)

    player.stop()
    player.release()

def play():
     while True:
        if not q.empty():
            file_path = q.get()
            print(f'Playing {file_path}')
            play_audio(file_path)
            os.remove(file_path)
        else:
            file = random.choice(os.listdir(STORED_PATH))
            file_path = os.path.join(STORED_PATH, file)
            print(f'Playing {file_path}')
            play_audio(file_path)

def search_download_queue(searchSTR):
    videosSearch = VideosSearch(searchSTR, limit=5)
    arr = videosSearch.result().get('result')
    for i in range(0, 5):
        try:
            yt = YouTube(arr[i]['link'])
            audio_stream = yt.streams.filter(only_audio=True).first()
            dl_path = audio_stream.download(output_path=DOWNLOAD_PATH)
            q.put(dl_path)
            print(f'The current playlist: {list(q.queue)}')
            break
        except Exception as e:
            print(f'An error occurred: {e}')

def main():
    audio_thread = threading.Thread(target=play)
    audio_thread.start()

    global NEXT_SONG, END_PROGRAM
    chat = pytchat.create(video_id=VIDEO_ID)
    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"{c.author.name}: {c.message}")
            if c.author.name not in SAVED_USERS:
                continue

            if c.message.startswith("!add "):
                searchSTR = c.message[5:]
                search_download_queue(searchSTR)
            elif c.message.startswith("!next"):
                NEXT_SONG = True
                
    audio_thread.join()

if __name__ == "__main__":
    main()
