from time import sleep
from shared import q, STORED_PATH, STOP_EVENT
import os, random, vlc, threading

def play_audio(file_path):
    player = vlc.MediaPlayer(file_path)
    player.play()

    sleep(5)
    while player.is_playing():
        sleep(1)
        if STOP_EVENT.is_set():
            STOP_EVENT.clear()
            break

    player.stop()
    player.release()

def main():
    while True:
        if q.empty():
            file = random.choice(os.listdir(STORED_PATH))
            file_path = STORED_PATH + '/' + file   
            audio_thread = threading.Thread(target=play_audio, args=(file_path))
            audio_thread.start()
            audio_thread.join()
        else:
            file_path = q.get()
            audio_thread = threading.Thread(target=play_audio, args=(file_path))
            audio_thread.start()
            audio_thread.join()
            os.remove(file_path)

if __name__ == "__main__":
    main()