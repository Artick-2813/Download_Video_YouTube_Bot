from pytube import YouTube


class DownloadVideoFromYouTube:

    def __init__(self, url):
        self.url = url

    def get_title_video(self):
        try:
            url = self.url
            yt = YouTube(url)
            title = yt.title
            return title

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
        url = self.url
        yt = YouTube(url)
        PATH = r'C:\Users\Admin\Desktop\Download_video'

        if quality == '720p':
            stream = yt.streams.get_by_itag(22)
            stream.download(output_path=PATH)
            return 'Видео загружено ✅'
        else:
            return 'Вы выбрали неправильное разрешение видео ❗'

    def download_video_360p(self, quality):
        url = self.url
        yt = YouTube(url)
        PATH = r'C:\Users\Admin\Desktop\Download_video'

        if quality == '360p':
            stream = yt.streams.get_by_itag(18)
            stream.download(output_path=PATH)
            return 'Видео загружено ✅'
        else:
            return 'Вы выбрали неправильное разрешение видео ❗'

    def download_video_144p(self, quality):
        url = self.url
        yt = YouTube(url)
        PATH = r'C:\Users\Admin\Desktop\Download_video'

        if quality == '144p':
            stream = yt.streams.get_by_itag(17)
            stream.download(output_path=PATH)
            return 'Видео загружено ✅'
        else:
            return 'Вы выбрали неправильное разрешение видео ❗'
