import telebot
from config import TOKEN
from Keyboard_Bot import menu_markup, cancel_markup, back_menu_markup, quality_menu
from Download_Handler import download_video

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, f'Привет {msg.chat.first_name} ✋\n'
                                  'Выбери что тебе нужно и мы начнем', reply_markup=menu_markup())


@bot.callback_query_handler(func=lambda call: call.data == 'Скачать видео')
def download_video_url(call):
    if call.data == 'Скачать видео':
        bot.send_message(call.message.chat.id, 'Введите URL видео',reply_markup=cancel_markup())
        bot.answer_callback_query(callback_query_id=call.id)

        @bot.message_handler(content_types=['text'])
        def get_url(msg):
            global save_url
            save_url = msg.text
            bot.send_message(chat_id=msg.chat.id, text='Выберите качество видео', reply_markup=quality_menu())

        @bot.callback_query_handler(func=lambda call: call.data == '720p' or call.data == '480p')
        def get_quality(call):
            if call.data == '720p':
                save_quality = call.data
                call_msg = call.message.chat.id

                bot.send_message(chat_id=call_msg, text='Подождите пожалуйста, видео загружается 🕜')
                upload_my_video = download_video(save_url, save_quality)
                bot.answer_callback_query(callback_query_id=call.id)
                bot.send_message(chat_id=call_msg, text=upload_my_video, reply_markup=back_menu_markup())

            if call.data == '480p':
                save_quality = call.data
                call_msg = call.message.chat.id

                bot.send_message(chat_id=call_msg, text='Подождите пожалуйста, видео загружается 🕜')
                upload_my_video = download_video(save_url, save_quality)
                bot.answer_callback_query(callback_query_id=call.id)
                bot.send_message(chat_id=call_msg, text=upload_my_video, reply_markup=back_menu_markup())
            else:
                bot.answer_callback_query(callback_query_id=call.id, text='Упс, возникла какая-то ошибка 😔',
                                          show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == 'Загрузка')
def download_video_url(call):

    if call.data == 'Загрузка':
        bot.send_message(call.message.chat.id, 'Загрузите видеофайл и я скачаю видео в телеграмм', reply_markup=cancel_markup())
        bot.answer_callback_query(callback_query_id=call.id)

        @bot.message_handler(content_types=['video'])
        def get_id(msg):
            try:
                video_id = msg.video.file_id
                my_chat_id = msg.chat.id

                bot.send_video(data=video_id, chat_id=my_chat_id)

                bot.send_message(my_chat_id, 'Видео загружено ✅', reply_markup=back_menu_markup())
            except Exception as ex:
                bot.send_message(chat_id=msg.chat.id, text='Упс, возникла какая-то ошибка :(')
                print('ERROR:', str(ex))


@bot.callback_query_handler(func=lambda call: call.data == 'Отмена')
def cancel(call):
    if call.data == 'Отмена':
        bot.send_message(text='Отмена', chat_id=call.message.chat.id, reply_markup=menu_markup())
        bot.answer_callback_query(callback_query_id=call.id)


@bot.callback_query_handler(func=lambda call: call.data == 'Назад')
def back(call):
    if call.data == 'Назад':
        bot.send_message(text='Возращаюсь назад', chat_id=call.message.chat.id, reply_markup=menu_markup())
        bot.answer_callback_query(callback_query_id=call.id)


bot.polling()