from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.utils import executor

bot = Bot(token="1223903928:AAFsuWXxkXGyNmcAGzLQS3aJ0dyy1VG9yDM")
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(state='*')
async def start_command(message: Message) -> None:
    print(message.text)
    await message.answer('Hello, mobster! How is ur mother?')


# Start the main process
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
