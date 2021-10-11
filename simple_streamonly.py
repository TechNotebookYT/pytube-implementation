# Only Downloads Specified Stream - Due to YouTube's new DASH Streaming Protocol,
# the Audio and Video on HD videos need to be downloaded separately

from pytube import YouTube

def download(yt_obj, stream_num):
    """
    Download Video
    ---------
    Downloads a YouTube Video with the inputs of the URL and the Stream Number (Itag)
    
    :param url: The URL of the Video
    :param stream_num: the itag of the video
    """

    yt_obj.streams.get_by_itag(stream_num).download() # Downloads the selected stream


def interface():
    """
    User Interface
    ---------------
    Command line Interface > allows user to enter values for [url] and [itag] for use in download()

    Keyword arguments: none
    Return: none
    """
    print("Python YouTube Downloader")
    url = input("URL: ")
    
    yt = YouTube(url) # Selects a video
    
    print("Loading...")
    # Printing all posible streams
    for i in list(yt.streams):
        print(i)

    itag = input("Itag: ") # Selecting a stream to download

    print('Downloading...')
    download(yt, itag) # Downloads stream (see downloads())
    print('Download Complete')

interface()
