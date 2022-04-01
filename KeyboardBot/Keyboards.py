from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def menu_markup():
    btn_download_video_url = KeyboardButton('Скачать видео по URL 📽')
    btn_download_audio_url = KeyboardButton('Загрузить аудиофайл 📀')
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(

        btn_download_video_url,
        btn_download_audio_url
    )

    return menu


def cancel_markup():
    btn_cancel = InlineKeyboardButton('Отмена ❌', callback_data='Отмена')
    cancel = InlineKeyboardMarkup().add(btn_cancel)

    return cancel


def back_menu_markup():
    btn_back = KeyboardButton('Назад в меню 🔙')
    back = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back)

    return back


def quality_menu():
    btn_quality_720 = KeyboardButton('720p')
    btn_quality_360 = InlineKeyboardButton('360p')
    btn_quality_144 = InlineKeyboardButton('144p')
    quality = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btn_quality_720, btn_quality_360,
                                                                         btn_quality_144)

    return quality
