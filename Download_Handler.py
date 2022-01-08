from pytube import YouTube


def download_video(url, quality):
    try:
        yt = YouTube(url)
        PATH = r'C:\Users\Admin\Desktop\Download_video'

        if quality == '720p':
            stream = yt.streams.get_by_itag(22)
            if not stream:
                return 'Такого разрешения не существует ❗'

            else:
                stream.download(output_path=PATH)
                return 'Видео загружено ✅'

        if quality == '480p':
            stream = yt.streams.get_by_itag(135)
            if not stream:
                return 'Такого разрешения не существует ❗'
            else:
                stream.download(output_path=PATH)
                return 'Видео загружено ✅'
        else:
            return 'Укажите разрешения видео ❗'
    except Exception as e:
        print('ERROR:', str(e))
        return 'Неправильный ввод url адреса ❗'