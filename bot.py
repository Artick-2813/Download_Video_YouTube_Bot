import logging
from aiogram import executor
from create_bot import dp

logging.basicConfig(level=logging.INFO)

from HandlersBot import start, download_video

start.register_handler_start(dp)
download_video.register_handlers_download_video(dp)


executor.start_polling(dp, skip_updates=True)
