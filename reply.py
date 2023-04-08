from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message, CallbackQuery
from aiogram.utils import executor

bot = Bot(token="1223903928:AAFsuWXxkXGyNmcAGzLQS3aJ0dyy1VG9yDM")
dp = Dispatcher(bot, storage=MemoryStorage())


def reply_main_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text='кнопа 1')
    button2 = KeyboardButton(text='кнопа 2')
    button3 = KeyboardButton(text='Ссылка')
    markup.add(button1).row(button2, button3)
    return markup



@dp.message_handler(commands=['start'], state='*')
async def start_command(message: Message) -> None:
    await message.answer('Hello, mobster! How is ur mother?', reply_markup=reply_main_markup())



@dp.message_handler(Text(equals='кнопа 1'), state='*')
async def but1(msg: Message):
    await msg.answer("Ты нажал на кнопку 1!")


@dp.message_handler(Text(equals='кнопа 2'), state='*')
async def but1(msg: Message):
    await msg.answer("Ты нажал на кнопку 2!")


# Start the main process
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
