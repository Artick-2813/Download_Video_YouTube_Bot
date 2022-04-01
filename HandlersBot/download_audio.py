from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot, dp
from KeyboardBot import Keyboards
from aiogram.types import ReplyKeyboardRemove
from Download_Handler import DownloadAudioFromYouTube

back_menu = Keyboards.back_menu_markup()
menu_markup = Keyboards.menu_markup()
quality_menu = Keyboards.quality_menu()


class Audio(StatesGroup):
    FILENAME = State()


async def download_audio(msg: types.Message):
    chat_id = msg.chat.id

    await Audio.FILENAME.set()
    await bot.send_message(chat_id, 'Введите название загруженного видео',
                           reply_markup=back_menu)


async def start_download_audio(msg: types.Message, state: FSMContext):

    save_file_name = msg.text
    chat_id = msg.chat.id

    await state.update_data(FILENAME=save_file_name)

    data = await state.get_data()

    file = data['FILENAME']

    file_name = file + '.mp4'

    await bot.send_message(chat_id, 'Подождите пожалуйста, идет загрузка 🕐', reply_markup=ReplyKeyboardRemove())

    audio = DownloadAudioFromYouTube(file_name).download_audio()

    await bot.send_message(chat_id, audio, reply_markup=menu_markup)

    @dp.message_handler(content_types=['audio'])
    async def download_audio_in_telegram(msg: types.Message):
        chat_id = msg.chat.id
        audio_id = msg.audio.file_id

        await bot.send_audio(chat_id, audio=audio_id)
        await bot.send_message(chat_id, 'Аудио загружено ✅', reply_markup=menu_markup)

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


def register_handlers_download_audio(dp: Dispatcher):

    dp.register_message_handler(download_audio, lambda call: call.text == 'Загрузить аудиофайл 📀')
    dp.register_message_handler(start_download_audio, state=Audio.FILENAME)

    dp.register_message_handler(menu_back, state="*", commands='Назад в меню 🔙')
    dp.register_message_handler(menu_back, Text(equals='Назад в меню 🔙', ignore_case=True), state="*")
