from pytube import YouTube


class DownloadVideoFromYouTube:

    def __init__(self, url):
        self.url = url

    def get_info_video(self):
        info = {}
        try:
            url = self.url
            yt = YouTube(url)

            title = yt.title
            views = yt.views
            author = yt.author

            info['title'] = title
            info['views'] = views
            info['author'] = author

            return f'📽 Видео: {info["title"]}\n' \
                   f'👁 Просмотры: {info["views"]}\n' \
                   f'🖍 Автор: {info["author"]}'

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
                return self.url

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
                return self.url
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
                return self.url
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

    def __init__(self, url):
        self.url = url

    def download_audio(self):
        try:
            url = self.url
            yt = YouTube(url)
            PATH = r'C:\Users\Admin\Desktop\Download_video'

            audio = yt.streams.filter(only_audio=True)
            audio[0].download(output_path=PATH)
            return 'Аудио загружено ✅'
        except Exception as e:
            print('ERROR:', str(e))
            return 'Не удалось получить URL адрес ❗'

# print(DownloadVideoFromYouTube('https://www.youtube.com/watch?v=vwT-IxAS_ss').get_info_video())
# print(DownloadVideoFromYouTube('tfeedd').download_video_720p('720p'))