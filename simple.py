from pytube import YouTube

def select_video(url):
    return YouTube(url)

def download(yt_obj, audio_only):
    if audio_only:
        yt_obj.streams.get_by_itag(140).download()
    else:
        yt_obj.streams.get_by_itag(137).download()

download(select_video('https://youtu.be/bg-quTTOeH4'), False)

