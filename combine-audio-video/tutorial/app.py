from pytube import YouTube
import ffmpeg
import os
import shutil

def merge(video_path, audio_path, file, final_path):
    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(audio_path)

    ffmpeg.output(video, audio, f'{final_path}/{file}', acodec='copy', vcodec='copy').run()

def interface():
    url = input("URL: ")
    
    yt = YouTube(url)

    CURR_DIR = os.path.dirname(os.path.realpath(__file__))

    path = os.path.join(CURR_DIR, 'downloads')
    
    yt.streams.get_highest_resolution().download(output_path=os.path.join(path, 'video'))
    yt.streams.get_audio_only().download(output_path=os.path.join(path, 'audio'))

    video_filename = os.listdir(os.path.join(path, 'video'))[0]

    video_filepath = f'{os.path.join(path, "video")}/{video_filename}'
    audio_filepath = f'{os.path.join(path, "audio")}/{video_filename}'

    merge(video_filepath, audio_filepath, video_filename, path)

    shutil.rmtree(os.path.join(path, 'video'))
    shutil.rmtree(os.path.join(path, 'audio'))

interface()
