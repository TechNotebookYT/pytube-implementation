# Imports
from pytube import YouTube
import os
import shutil
import ffmpeg


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


def interface():
    """
    User interface - Through the command line
    """
    url = input("URL: ")  # User inputs the URL of the YouTube Video

    yt = YouTube(url)  # Initializes YouTube object

    # Uses os module to get path to file
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))

    # creates download folder and sets it as path
    path = os.path.join(CURR_DIR, 'downloads')

    # Video Stream
    yt.streams.get_highest_resolution().download(os.path.join(path, 'video'))
    # Audio Stream
    yt.streams.get_by_itag(139).download(os.path.join(path, 'audio'))

    # Gets the name of the downloaded files using the file in the video directory
    video_filename = os.listdir(os.path.join(path, 'video'))[0]

    # Calls the merge function
    merge(f'{os.path.join(path, "video")}/{video_filename}',
          f'{os.path.join(path, "audio")}/{video_filename}', video_filename, path)

    # Deletes the video and audio directories
    shutil.rmtree(os.path.join(path, 'audio'))
    shutil.rmtree(os.path.join(path, 'video'))


interface()
