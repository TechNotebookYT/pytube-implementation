from pytube import YouTube

def interface():
    print("Welcome to the Pytube Downloader!")
    url = input("URL: ")

    yt = YouTube(url)

    for i in list(yt.streams):
        print(i)


    itag = input("Itag of Video: ")
    yt.streams.get_by_itag(int(itag)).download()

interface()