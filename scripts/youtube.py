from colorama import Fore, Back, Style
import click
from pytube import Playlist, YouTube
import ffmpeg


def clear_filename(name):
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

@click.command()
@click.option('--type', default='video', help='video (Single video) | playlist (whole playlist)')
@click.option('--link', prompt='Link', help='Link of the video/playlist')
def download(type, link):
    if (type == 'video'):
        return download_single_video(link)
    return download_playlist(link)


@download_logger
def download_single_video(link):
    yt = YouTube(link)
    filename = clear_filename(yt.title)
    click.echo(filename)
    if (not os.path.exists(filename)):
        try:
            download_audio(yt)
            download_video(yt)
            mix_video(filename)
        except Exception as error:
            raise error
        finally:
            clear_mockups()


def download_playlist(link):
    playlist = Playlist(link)
    for link in playlist.video_urls:
        download_single_video(link)

if __name__ == '__main__':
    download()
