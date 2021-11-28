# Imports
from tkinter import *
from pytube import YouTube
import os
import shutil
import ffmpeg

# Uses os module to get path to file
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
# location of downloads folder
dnld_path = os.path.join(CURR_DIR, 'downloads')


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

def download(url):
    ''' Downloads the video and audio streams'''

    yt = YouTube(url)  # Initializes YouTube object

    # Video Stream
    yt.streams.get_highest_resolution().download(os.path.join(dnld_path, 'video'))
    # Audio Stream
    yt.streams.get_by_itag(139).download(os.path.join(dnld_path, 'audio'))

    # Gets the name of the downloaded files using the file in the video directory
    return os.listdir(os.path.join(dnld_path, 'video'))[0]

def cleanup():
    ''' Deletes the video and audio directories '''
    shutil.rmtree(os.path.join(dnld_path, 'audio'))
    shutil.rmtree(os.path.join(dnld_path, 'video'))

# def main():
#     download(<url here>)
#     merge(f'{os.path.join(dnld_path, "video")}/{video_filename}',
#           f'{os.path.join(dnld_path, "audio")}/{video_filename}', video_filename, dnld_path)

#     #


# main()


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("Pytube Downloader")
root.geometry('300x300')

# show window
root.mainloop()

