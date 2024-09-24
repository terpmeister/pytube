
from pytubefix import Playlist
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/playlist?list=PLzpn_IJe2P-ROevCQVyY3wegcHx-R0v3L"

pl = Playlist(url)

for video in pl.videos:
    # ys = video.streams.get_audio_only()
    # ys.download(mp3=True)
    print(video.title)
 
    ys = video.streams.get_highest_resolution()
    ys.download()