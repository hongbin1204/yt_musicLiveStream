from youtubesearchpython import VideosSearch
from pytubefix import YouTube
from shared import DOWNLOAD_PATH, SAVED_USERS, STOP_EVENT, VIDEO_ID, q
import pytchat

def searchDownloadQueue(searchSTR):
    videosSearch = VideosSearch(searchSTR, limit = 5)
    arr = videosSearch.result().get('result')
    for i in range(0,5):
        try: 
            yt = YouTube(arr[i]['link'])
            audio_stream = yt.streams.filter(only_audio=True).first()
            dl_path = audio_stream.download(output_path=DOWNLOAD_PATH)
            q.put(dl_path)
            break
        except Exception as e:
            print(f'an error occured: {e}')

def main():
    chat = pytchat.create(video_id=VIDEO_ID)
    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"{c.author.name}: {c.message}")
            if not c.author.name in SAVED_USERS:
                continue

            if c.message[0:5] == "!add ":
                searchDownloadQueue(c.message[5:])
            elif c.message[0:5] == "!next":
                STOP_EVENT.set()

if __name__ == "__main__":
    main()