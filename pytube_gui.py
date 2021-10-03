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
    returns: a dictionary that contains yt_obj & streams
    """
    yt = YouTube(url)
    return {
        'yt_obj': yt,
        'streams': list(yt.streams)
    }


class Application(tk.Frame):
    """
    Application
    -------
    The main class for the tkinter app
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        # This holds a string full of the streams (see ln 76)
        self.streams = ''

    def create_widgets(self):
        """
        Widgets
        --------
        Houses all the elements on the tkinter app
        """

        self.urllabel = tk.Label(root, text='URL')
        self.urllabel.pack(side='top')

        # Field to enter URL
        self.urlwidget = tk.Text(root, height=2)
        self.urlwidget.pack(side='top')

        # Button that runs show_streams() and passes in the value of the URL field
        self.trigger_get_streams = tk.Button(
            root, text="Get Streams", command=lambda: self.show_streams(self.urlwidget.get("1.0", "end-1c")))
        self.trigger_get_streams.pack(side='top')

        # This will show streams once the show_streams method is called
        self.stream_lbl = tk.Label(root, text="")
        self.stream_lbl.pack(side='top')

        self.streamfield_label = tk.Label(root, text='Stream #')
        self.streamfield_label.pack(side='top')
        
        # Field to enter the stream # (itag)
        self.streamfield = tk.Text(root, height=2)
        self.streamfield.pack(side='top')

        # Button that calls the download function with the yt_obj and the content of streamfield
        self.download = tk.Button(
            self, text="Download", fg="blue", command=lambda: download(self.yt_obj, self.streamfield.get("1.0", "end-1c")))
        self.download.pack(side='top')

    def show_streams(self, url):
        """
        Show Streams
        ------
        Calls the get_yt_obj_and_streams() func w/ the url & parses output.
        Modifies the stream label to show all the possible streams

        Keyword arguments:
        url -- The URL of the video
        """
        
        yt_output = get_yt_obj_and_streams(url)
        for i in yt_output['streams']: # Adds each element in the list to a string with newlines
            self.streams += str(i)
            self.streams += '\n'
        self.yt_obj = yt_output['yt_obj']

        self.stream_lbl.config(text="Streams: \n" + self.streams)


root = tk.Tk() # Creating the main window
root.title("Pytube")
root.geometry("1200x600")

app = Application(master=root)
app.mainloop()
