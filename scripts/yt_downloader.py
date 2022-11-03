from colorama import Fore, Back, Style
from pytube import Playlist, YouTube
import ffmpeg
from sys import argv
import os


def clean_filename(name):
    forbidden_chars = '"*\\/\'.|?:<>'
    filename = (''.join(
        [x if x not in forbidden_chars else '#' for x in name]
    )) \
        .replace('á', 'a') \
        .replace('â', 'a') \
        .replace('ã', 'a') \
        .replace('é', 'e') \
        .replace('ê', 'e') \
        .replace('ç', 'c') \
        .replace('ô', 'o') \
        .replace('õ', 'o') \
        .replace('  ', ' ').strip()
    if len(filename) >= 176:
        filename = filename[:170] + '...'
    return f'{filename}.mp4'


def download_logger(func):
    def wrapper(*args, **kwargs):
        print(Fore.GREEN + 'Starting Download')
        print(Style.RESET_ALL)
        result = func(*args, **kwargs)
        print(Fore.WHITE + Back.GREEN + 'Download Finished')
        print(Style.RESET_ALL)
        return result
    return wrapper


def download_audio(yt):
    yt.streams \
        .filter(abr="160kbps", progressive=False) \
        .first() \
        .download(filename="audio.mp3")


def download_video(yt):
    video_streamer = yt.streams \
        .filter(res='720p', progressive=False) \
        .first()
    if (not video_streamer):
        video_streamer = yt.streams \
            .filter(res='480p', progressive=False) \
            .first()
    if (not video_streamer):
        video_streamer = yt.streams \
            .filter(res='360p', progressive=False) \
            .first()
    video_streamer.download(filename='video.mp4')


def mix_video(filename):
    audio = ffmpeg.input('audio.mp3')
    video = ffmpeg.input('video.mp4')
    ffmpeg.output(audio, video, filename).run(overwrite_output=True)


def clear_mockups():
    if (os.path.exists('audio.mp3')):
        os.remove('audio.mp3')
    if (os.path.exists('video.mp4')):
        os.remove('video.mp4')


@download_logger
def download(link):
    yt = YouTube(link)
    filename = clean_filename(yt.title)
    print(filename)
    if (not os.path.exists(filename)):
        try:
            download_audio(yt)
            download_video(yt)
            mix_video(filename)
        except Exception as error:
            raise error
        finally:
            clear_mockups()


def download_playlist(playlist):
    for link in playlist.video_urls:
        download(link)


if (argv[1] == '-p' or argv[1] == '--playlist'):
    playlist = Playlist(argv[2])
    download_playlist(playlist)
elif (argv[1] == '-v' or argv[1] == '--video'):
    download(argv[2])
else:
    print(Fore.RED + 'Invalid Option')
    print(Style.RESET_ALL)
