from pytube import YouTube


def copy(video_path, audio_path, name, final_path):
    """
    FFMPEG-COPY
    ------

    video_path: path of video on disk
    audio_path: path of audio on disk
    name: name of output file
    final_path: path of output video on disk
    """
    import ffmpeg
    video = ffmpeg.input(audio_path)
    audio = ffmpeg.input(video_path)
    (
        ffmpeg
        .output(audio, video, f'{name}.mp4', acodec='copy', vcodec='copy')
        .run()
    )
