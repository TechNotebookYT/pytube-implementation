def copy(video_path, audio_path, final_path, name):
    import ffmpeg
    video = ffmpeg.input(audio_path)
    audio = ffmpeg.input(video_path)
    (
        ffmpeg
        .output(audio, video, f'{name}.mp4', acodec='copy', vcodec='copy')
        .run()
    )
