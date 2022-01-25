from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def menu_markup():
    btn_download_video_url = InlineKeyboardButton('Скачать видео по URL 📽', callback_data='Скачать видео')
    btn_download_video_id = InlineKeyboardButton('Загрузка видео 📩', callback_data='Загрузка')
    btn_download_audio_url = InlineKeyboardButton('Загрузка аудио по URL 💽', callback_data='Загрузка аудио')
    btn_download_audio_id = InlineKeyboardButton('Загрузка аудио', callback_data='Загрузка аудио по id')
    menu = InlineKeyboardMarkup(row_width=2).add(btn_download_video_url, btn_download_video_id,
                                                 btn_download_audio_url, btn_download_audio_id)

    return menu


def cancel_markup():
    btn_cancel = InlineKeyboardButton('Отмена ❌', callback_data='Отмена')
    cancel = InlineKeyboardMarkup().add(btn_cancel)

    return cancel


def back_menu_markup():
    btn_back = InlineKeyboardButton('Назад в меню 🔙', callback_data='Назад')
    back = InlineKeyboardMarkup().add(btn_back)

    return back


def quality_menu():
    btn_quality_720 = InlineKeyboardButton('720p', callback_data='720p')
    btn_quality_360 = InlineKeyboardButton('360p', callback_data='360p')
    btn_quality_144 = InlineKeyboardButton('144p', callback_data='144p')
    quality = InlineKeyboardMarkup(row_width=2).add(btn_quality_720, btn_quality_360, btn_quality_144)

    return quality
