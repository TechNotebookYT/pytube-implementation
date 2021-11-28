# Imports
import tkinter as tk
from pytube import YouTube
import os
import shutil
import ffmpeg

# vars
# Uses os module to get path to file
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
# location of downloads folder
dnld_path = os.path.join(CURR_DIR, 'downloads')

def download(url):
    ''' Downloads the video and audio streams into different directories'''

    yt = YouTube(url)  # Initializes YouTube object

    # Video Stream
    yt.streams.get_highest_resolution().download(os.path.join(dnld_path, 'video'))
    # Audio Stream
    yt.streams.get_by_itag(139).download(os.path.join(dnld_path, 'audio'))

    # Gets the name of the downloaded files using the file in the video directory
    return os.listdir(os.path.join(dnld_path, 'video'))[0]


def merge(video_path, audio_path, file, final_path):
    """
    FFMPEG-Merge
    ------
    video_path: path of video on disk
    audio_path: path of audio on disk
    name: name of output file
    final_path: path of output video on disk
    """
    # adds the video and audio as an input for ffmpeg
    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(audio_path)

    # Runs the FFMPEG module to join the audio and video
    ffmpeg.output(
        video, audio, f'{final_path}/{file}', acodec='copy', vcodec='copy').run()


def cleanup():
    ''' Deletes the video and audio directories '''
    shutil.rmtree(os.path.join(dnld_path, 'audio'))
    shutil.rmtree(os.path.join(dnld_path, 'video'))


def main(url):
    if url == '':
        return
    download(url)
    video_filename = os.listdir(os.path.join(dnld_path, 'video'))[0]
    merge(f'{os.path.join(dnld_path, "video")}/{video_filename}',
          f'{os.path.join(dnld_path, "audio")}/{video_filename}', video_filename, dnld_path)
    cleanup()

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

    def create_widgets(self):
        """
        Widgets
        --------
        Houses all the elements on the tkinter app
        """

        self.urllabel = tk.Label(root, text='URL')
        self.urllabel.pack(side='top')

        # Field to enter URL
        self.urlfield = tk.Text(root, height=2)
        self.urlfield.pack(side='top')

        # Button that calls the download function with the yt_obj and the content of streamfield
        self.download = tk.Button(
            self, text="Download", fg="blue", command=lambda: main(self.urlfield.get("1.0", "end-1c")))
        self.download.pack(side='top')

root = tk.Tk()  # Creating the main window
root.title("Pytube")
root.geometry("1200x600")

app = Application(master=root)
app.mainloop()
