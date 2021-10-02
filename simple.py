from pytube import YouTube

def download(youtube_obj, stream_num):
    """
    Download Video
    ---------
    Downloads a YouTube Video with the inputs of the URL and the Stream Number (Itag)
    
    :param url: The URL of the Video
    :param stream_num: the itag of the video
    """

    youtube_obj.streams.get_by_itag(stream_num).download()


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
    
    yt = YouTube(url)
    
    print("Loading...")
    for i in list(yt.streams):
        print(i)

    itag = input("Itag: ")

    print('Downloading...')
    download(yt, itag)
    print('Download Complete')

interface()