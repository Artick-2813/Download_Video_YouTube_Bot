from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot, dp
from KeyboardBot import Keyboards
from aiogram.types import ReplyKeyboardRemove
from Download_Handler import DownloadVideoFromYouTube, DownloadAudioFromYouTube

back_menu = Keyboards.back_menu_markup()
menu_markup = Keyboards.menu_markup()
quality_menu = Keyboards.quality_menu()


class Video(StatesGroup):
    URL_VIDEO = State()
    QUALITY = State()


async def download_video_url(msg: types.Message):
        chat_id = msg.chat.id

        await Video.URL_VIDEO.set()
        await bot.send_message(chat_id, 'Введите URL видео', reply_markup=back_menu)


async def get_quality(msg: types.Message, state: FSMContext):
    save_url = msg.text
    chat_id = msg.chat.id

    await state.update_data(URL_VIDEO=save_url)
    await bot.send_message(chat_id, 'Выбери качество видео', reply_markup=quality_menu)

    await Video.QUALITY.set()


async def start_download_video(msg: types.Message, state: FSMContext):
    save_quality = msg.text
    chat_id = msg.chat.id

    await state.update_data(QUALITY=save_quality)

    data = await state.get_data()

    url = data['URL_VIDEO']
    quality = data['QUALITY']

    if quality == '720p':

        await bot.send_message(chat_id, 'Начинаю загрузку видео 🕐', reply_markup=ReplyKeyboardRemove())
        upload_video = DownloadVideoFromYouTube(url).download_video_720p(save_quality)

        if upload_video == 'Видео загружено':
            global video_title

            video_title = DownloadVideoFromYouTube(url).get_title_video()

            await bot.send_message(chat_id, text='Видео загружено ✅')
            await bot.send_message(chat_id, text='Загрузите скаченный видеофайл сюда')

            @dp.message_handler(content_types=['video'])
            async def download_video_in_telegram(msg: types.Message):
                chat_id = msg.chat.id
                video_id = msg.video.file_id

                await bot.send_video(chat_id, video=video_id, caption=video_title)
                await bot.send_message(chat_id, 'Видео загружено ✅', reply_markup=menu_markup)

            await state.finish()

        else:
            text = f'Видео не загружено ❌ \n' \
                   f'{upload_video}'
            await bot.send_message(chat_id, text=text, reply_markup=menu_markup)
            await state.finish()

    if quality == '360p':

        await bot.send_message(chat_id, 'Начинаю загрузку видео 🕐', reply_markup=ReplyKeyboardRemove())
        upload_video = DownloadVideoFromYouTube(url).download_video_360p(save_quality)

        if upload_video == 'Видео загружено':

            video_title = DownloadVideoFromYouTube(url).get_title_video()

            await bot.send_message(chat_id, text='Видео загружено ✅')
            await bot.send_message(chat_id, text='Загрузите скаченный видеофайл сюда')

            @dp.message_handler(content_types=['video'])
            async def download_video_in_telegram(msg: types.Message):
                chat_id = msg.chat.id
                video_id = msg.video.file_id

                await bot.send_video(chat_id, video=video_id, caption=video_title)
                await bot.send_message(chat_id, 'Видео загружено ✅', reply_markup=menu_markup)

            await state.finish()

        else:
            text = f'Видео не загружено ❌ \n' \
                   f'{upload_video}'
            await bot.send_message(chat_id, text=text, reply_markup=menu_markup)
            await state.finish()

    if quality == '144p':

        await bot.send_message(chat_id, 'Начинаю загрузку видео 🕐', reply_markup=ReplyKeyboardRemove())
        upload_video = DownloadVideoFromYouTube(url).download_video_144p(save_quality)

        if upload_video == 'Видео загружено':

            video_title = DownloadVideoFromYouTube(url).get_title_video()

            await bot.send_message(chat_id, text='Видео загружено ✅')
            await bot.send_message(chat_id, text='Загрузите скаченный видеофайл сюда')

            @dp.message_handler(content_types=['video'])
            async def download_video_in_telegram(msg: types.Message):
                chat_id = msg.chat.id
                video_id = msg.video.file_id

                await bot.send_video(chat_id, video=video_id, caption=video_title)
                await bot.send_message(chat_id, 'Видео загружено ✅', reply_markup=menu_markup)

            await state.finish()

        else:
            text = f'Видео не загружено ❌ \n' \
                   f'{upload_video}'
            await bot.send_message(chat_id, text=text, reply_markup=menu_markup)
            await state.finish()


@dp.message_handler(state="*", commands='Назад в меню 🔙')
@dp.message_handler(Text(equals='Назад в меню 🔙', ignore_case=True), state="*")
async def menu_back(msg: types.Message, state: FSMContext):
        current_state = await state.get_state()
        chat_id = msg.chat.id
        if current_state is None:
            return
        await state.finish()
        await bot.send_message(chat_id, 'Возрващаюсь в меню', reply_markup=menu_markup)


def register_handlers_download_video(dp: Dispatcher):
    dp.register_message_handler(download_video_url, lambda call: call.text == 'Скачать видео по URL 📽')
    dp.register_message_handler(get_quality, state=Video.URL_VIDEO)
    dp.register_message_handler(start_download_video, state=Video.QUALITY)

    dp.register_message_handler(menu_back, state="*", commands='Назад в меню 🔙')
    dp.register_message_handler(menu_back, Text(equals='Назад в меню 🔙', ignore_case=True), state="*")



