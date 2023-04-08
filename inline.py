import time

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery
from aiogram.utils import executor

bot = Bot(token="1223903928:AAFsuWXxkXGyNmcAGzLQS3aJ0dyy1VG9yDM")
dp = Dispatcher(bot, storage=MemoryStorage())


def main_markup():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='кнопа 1', callback_data='but1')
    button2 = InlineKeyboardButton(text='кнопа 2', callback_data='but2')
    button3 = InlineKeyboardButton(text='Ссылка', url='https://sky.pro/')
    markup.row(button1, button2, button3)
    return markup



@dp.message_handler(commands=['start'], state='*')
async def start_command(message: Message) -> None:
    await message.answer('Hello, mobster! How is ur mother?', reply_markup=main_markup())
    # await bot.send_message(chat_id=message.chat.id, text='1231321', reply_markup=main_markup())



@dp.callback_query_handler(text='but1', state='*')
async def but1(call: CallbackQuery):
    a = await call.message.answer('adffsdfsfd')
    await call.message.answer("Ты нажал на кнопку 1!")
    await asyncio.sleep(3)
    await a.delete()


@dp.callback_query_handler(text='but2', state='*')
async def but1(call: CallbackQuery):
    await call.message.answer("Ты нажал на кнопку 2!")


# Start the main process
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
