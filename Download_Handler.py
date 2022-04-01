from pytube import YouTube
from moviepy.editor import AudioFileClip

import os


class DownloadVideoFromYouTube:

    def __init__(self, url):
        self.url = url

    def get_title_video(self):
        info = {}
        try:
            url = self.url
            yt = YouTube(url)

            title = yt.title

            info['title'] = title

            return f'📽 Видео: {info["title"]}'

        except Exception as e:
            print('ERROR:', str(e))
            return 'Неправильный ввод url адреса ❗'

    def get_url_video(self):
        try:
            url_video = self.url
            return url_video
        except Exception as e:
            print('ERROR:', str(e))
            return 'Не удалось получить URL адрес ❗'

    def download_video_720p(self, quality):
        try:
            url = self.url
            yt = YouTube(url)

            PATH = r'C:\Users\Admin\Desktop\Download_video'

            if quality == '720p':
                stream = yt.streams.get_by_itag(22)
                stream.download(output_path=PATH)
                return 'Видео загружено'

            else:
                return 'Такого разрешения нет ❗'
        except Exception as ex:

            if str(ex) == 'regex_search: could not find match for (?:v=|\/)([0-9A-Za-z_-]{11}).*':
                print('ERROR: ', ex)
                return 'Неправильный ввод адреса видео'

            if str(ex) == "'NoneType' object has no attribute 'download'":
                print('ERROR: ', ex)
                return 'Такого разрешения нет ❗'
            else:
                print(str(ex))
                return 'Упс, возникла какая-то ошибка :('

    def download_video_360p(self, quality):
        try:
            url = self.url
            yt = YouTube(url)

            PATH = r'C:\Users\Admin\Desktop\Download_video'

            if quality == '360p':
                stream = yt.streams.get_by_itag(18)
                stream.download(output_path=PATH)
                return 'Видео загружено'
            else:
                return 'Такого разрешения нет ❗'
        except Exception as ex:

            if str(ex) == 'regex_search: could not find match for (?:v=|\/)([0-9A-Za-z_-]{11}).*':
                print('ERROR: ', ex)
                return 'Неправильный ввод адреса видео'

            if str(ex) == "'NoneType' object has no attribute 'download'":
                print('ERROR: ', ex)
                return 'Такого разрешения нет ❗'
            else:
                print(str(ex))
                return 'Упс, возникла какая-то ошибка :('

    def download_video_144p(self, quality):
        try:
            url = self.url
            yt = YouTube(url)

            PATH = r'C:\Users\Admin\Desktop\Download_video'

            if quality == '144p':
                stream = yt.streams.get_by_itag(17)
                stream.download(output_path=PATH)
                return 'Видео загружено'
            else:
                return 'Такого разрешения нет ❗'
        except Exception as ex:

            if str(ex) == 'regex_search: could not find match for (?:v=|\/)([0-9A-Za-z_-]{11}).*':
                print('ERROR: ', ex)
                return 'Неправильный ввод адреса видео'

            if str(ex) == "'NoneType' object has no attribute 'download'":
                print('ERROR: ', ex)
                return 'Такого разрешения нет ❗'
            else:
                print(str(ex))
                return 'Упс, возникла какая-то ошибка :('


class DownloadAudioFromYouTube:

    def __init__(self, name_file):
        self.name_file = name_file

    def download_audio(self):
        try:
            PATH = r'C:\Users\Admin\Desktop\Download_video'

            file = self.name_file

            new_file = file.split('.')[0]

            full_path = os.path.join(PATH, file)
            print(full_path)

            audio = AudioFileClip(full_path)

            end_path = os.path.join(PATH, new_file + '.mp3')

            audio.write_audiofile(end_path)

            return 'Загрузка завершена, пожалуйста загрузите аудиофайл'
        except Exception as ex:
            print(ex)
            return 'К сожалению, не удалось загрузить аудиофайл'

