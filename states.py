from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

bot = Bot(token="6132535547:AAFVeBkfyiHmRCO4qO_fzzIz7_PkBMUMQzk")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    name = State()
    age = State()

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Давай знакомиться. Как тебя зовут?")
    await Form.name.set()

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        print(data)
        data["name"] = message.text

    await message.answer("Сколько тебе лет?")
    await Form.next()

@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text

    text = f"Пользователь {data['name']} возрастом {data['age']} зарегистрирован"
    await message.answer(text)

    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



# Простота
# Предсказуемость
# Легкая диагностика ошибок
# Легкость модификации
# Скорость