from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.utils import executor

bot = Bot(token="1223903928:AAFsuWXxkXGyNmcAGzLQS3aJ0dyy1VG9yDM")
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(state="*")
async def echo(message: Message) -> None:
    await bot.send_message(chat_id=message.chat.id, text=message.text)

    # Отправка музыки и картинки
    await bot.send_audio(chat_id=message.chat.id, audio=open("audio.mp3", "rb"))
    await bot.send_photo(chat_id=message.chat.id, photo=open("picture.png", "rb"))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)