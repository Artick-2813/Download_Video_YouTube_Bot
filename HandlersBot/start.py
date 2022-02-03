from create_bot import bot, dp
from aiogram import types, Dispatcher
from KeyboardBot import Keyboards


menu_markup = Keyboards.menu_markup()


async def start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.chat.first_name

    await bot.send_message(chat_id, f'Привет {first_name} ✋\n'
                                    'Выбери что тебе нужно и мы начнем', reply_markup=menu_markup)


def register_handler_start(dp: Dispatcher ):
    dp.register_message_handler(start, commands=['start'])