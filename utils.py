import requests
from pytube import YouTube
import os

def yt_search(query, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": api_key,
        "maxResults": 1,
        "type": "video"
    }
    r = requests.get(url, params=params).json()

    if "items" not in r or len(r["items"]) == 0:
        return None

    video_id = r["items"][0]["id"]["videoId"]
    title = r["items"][0]["snippet"]["title"]
    return {"video_id": video_id, "title": title}


def download_mp3(video_id):
    try:
        yt = YouTube(f"https://youtu.be/{video_id}")
        stream = yt.streams.filter(only_audio=True).first()
        file = stream.download(filename="song.mp4")

        mp3 = "song.mp3"
        os.system(f"ffmpeg -i song.mp4 -vn -ab 128k -ar 44100 -y {mp3}")

        os.remove("song.mp4")
        return mp3
    except Exception:
        return None
