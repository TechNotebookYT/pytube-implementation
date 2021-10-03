import tkinter as tk
from pytube import YouTube

def download(youtube_obj, stream_num):
    """
    Download Video
    ---------
    Downloads a YouTube Video with the inputs of the YouTube object and the Stream Number (Itag)
    
    :param youtube_obj: The YouTube object generated w/ the video URL
    :param stream_num: the itag of the video
    """

    # Downloads the selected stream
    youtube_obj.streams.get_by_itag(stream_num).download()

def get_yt_obj_and_streams(url):
    """
    Get Streams
    ---------
    Returns a dictionary that contains the YouTube object for the video as well as the streams

    To access yt_obj: key = ['yt_obj]
    To access streams: key = ['streams']
    
    :param url: The URL of the Video
    """
    yt = YouTube(url)
    return {
        'yt_obj': yt,
        'streams': list(yt.streams)
    }


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.streams = ''

    def create_widgets(self):
        self.urllabel = tk.Label(root, text='URL')
        self.urllabel.pack(side='top')

        self.urlwidget = tk.Text(root, height=2)
        self.urlwidget.pack(side='top')

        self.trigger_get_streams = tk.Button(
            root, text="Get Streams", command=lambda: self.show_streams(self.urlwidget.get("1.0", "end-1c")))
        self.trigger_get_streams.pack(side='top')

        self.stream_lbl = tk.Label(root, text="") # This will show streams once the show_streams method is called
        self.stream_lbl.pack(side='top')

        self.streamfield_label = tk.Label(root, text='Stream #')
        self.streamfield_label.pack(side='top')

        self.streamfield = tk.Text(root, height=2)
        self.streamfield.pack(side='top')

        self.download = tk.Button(
            self, text="Download", fg="blue", command=lambda: download(self.yt_obj, self.streamfield.get("1.0", "end-1c")))
        self.download.pack(side='top')

    def show_streams(self, url):
        yt_output = get_yt_obj_and_streams(url)
        for i in yt_output['streams']:
            self.streams += str(i)
            self.streams += '\n'
        self.yt_obj = yt_output['yt_obj']

        self.stream_lbl.config(text="Streams: \n" + self.streams)


root = tk.Tk()
root.title("Pytube")
root.geometry("300x300")

app = Application(master=root)
app.mainloop()
