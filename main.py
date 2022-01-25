import telebot
from config import TOKEN
from Keyboard_Bot import menu_markup, cancel_markup, back_menu_markup, quality_menu
from Download_Handler import DownloadVideoFromYouTube, DownloadAudioFromYouTube

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, f'Привет {msg.chat.first_name} ✋\n'
                                  'Выбери что тебе нужно и мы начнем', reply_markup=menu_markup())


@bot.callback_query_handler(func=lambda call: call.data == 'Скачать видео')
def download_video_url(call):
    if call.data == 'Скачать видео':
        bot.send_message(call.message.chat.id, 'Введите URL видео', reply_markup=cancel_markup())
        bot.answer_callback_query(callback_query_id=call.id)

        @bot.message_handler(content_types=['text'])
        def get_url_for_video(msg):

            global save_url
            global title_video

            save_url = msg.text
            title_video = DownloadVideoFromYouTube(save_url).get_title_video()

            bot.send_message(chat_id=msg.chat.id, text='Выберите качество видео', reply_markup=quality_menu())

        @bot.callback_query_handler(func=lambda call: call.data == '720p')
        def get_quality_720(call):

            if call.data == '720p':

                save_quality = call.data
                call_msg = call.message.chat.id

                bot.send_message(chat_id=call_msg, text='Подождите пожалуйста, видео загружается 🕜')
                upload_my_video = DownloadVideoFromYouTube(save_url).download_video_720p(save_quality)
                bot.answer_callback_query(callback_query_id=call.id)
                bot.send_message(chat_id=call_msg, text=upload_my_video, reply_markup=back_menu_markup())

        @bot.callback_query_handler(func=lambda call: call.data == '360p')
        def get_quality_360(call):

            if call.data == '360p':
                save_quality = call.data
                call_msg = call.message.chat.id

                bot.send_message(chat_id=call_msg, text='Подождите пожалуйста, видео загружается 🕜')
                upload_my_video = DownloadVideoFromYouTube(save_url).download_video_360p(save_quality)
                bot.answer_callback_query(callback_query_id=call.id)
                bot.send_message(chat_id=call_msg, text=upload_my_video, reply_markup=back_menu_markup())

        @bot.callback_query_handler(func=lambda call: call.data == '144p')
        def get_quality_144(call):

            if call.data == '144p':
                save_quality = call.data
                call_msg = call.message.chat.id

                bot.send_message(chat_id=call_msg, text='Подождите пожалуйста, видео загружается 🕜')
                upload_my_video = DownloadVideoFromYouTube(save_url).download_video_144p(save_quality)
                bot.answer_callback_query(callback_query_id=call.id)
                bot.send_message(chat_id=call_msg, text=upload_my_video, reply_markup=back_menu_markup())


@bot.callback_query_handler(func=lambda call: call.data == 'Загрузка')
def download_video_id(call):

    if call.data == 'Загрузка':
        bot.send_message(call.message.chat.id, 'Загрузите видеофайл и я скачаю видео в Телеграмм',
                         reply_markup=cancel_markup())
        bot.answer_callback_query(callback_query_id=call.id)

        @bot.message_handler(content_types=['video'])
        def get_video_id(msg):
            try:
                video_id = msg.video.file_id
                my_chat_id = msg.chat.id

                bot.send_video(data=video_id, chat_id=my_chat_id, caption=title_video)

                bot.send_message(my_chat_id, 'Видео загружено ✅', reply_markup=back_menu_markup())
            except Exception as ex:
                bot.send_message(chat_id=msg.chat.id, text='Упс, возникла какая-то ошибка :(')
                print('ERROR:', str(ex))


@bot.callback_query_handler(func=lambda call: call.data == 'Загрузка аудио')
def download_audio(call):
    id = call.message.chat.id

    if call.data == 'Загрузка аудио':
        bot.send_message(id, 'Введите URL видео, чтобы я начал загрузку аудио')
        bot.answer_callback_query(callback_query_id=call.id)

        @bot.message_handler(content_types=['text'])
        def get_url_for_audio(msg):
            global save_url

            save_url = msg.text
            upload_audio = DownloadAudioFromYouTube(save_url).download_audio()
            bot.send_message(msg.chat.id, upload_audio, reply_markup=back_menu_markup())


@bot.callback_query_handler(func=lambda call: call.data == 'Загрузка аудио по id')
def download_audio_id(call):

    if call.data == 'Загрузка аудио по id':
        bot.send_message(call.message.chat.id, 'Загрузите аудиофайл и я скачаю видео в Телеграмм',
                         reply_markup=cancel_markup())
        bot.answer_callback_query(callback_query_id=call.id)

        @bot.message_handler(content_types=['audio'])
        def get_audio_id(msg):
            try:
                audio_id = msg.audio.file_id
                my_chat_id = msg.chat.id

                bot.send_audio(audio=audio_id, chat_id=my_chat_id)
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