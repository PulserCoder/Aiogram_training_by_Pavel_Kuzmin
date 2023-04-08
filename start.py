from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message
from aiogram.utils import executor

bot = Bot(token="Token")
dp = Dispatcher(bot, storage=MemoryStorage())


# another realization
@dp.message_handler(commands=['start'], state="*")
# @dp.message_handler(CommandStart(), state='*')
async def start_command(message: Message) -> None:
    # await message.answer('Hello, mobster!')
    await bot.send_message(chat_id=message.chat.id, text='Hello, mobster!')

# Start the main process
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
