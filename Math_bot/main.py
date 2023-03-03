import logging
import pathlib
import asyncio
# noinspection PyUnresolvedReferences
from aiogram import Bot, Dispatcher, types, executor
from configparser import ConfigParser
# noinspection PyUnresolvedReferences
from logic import get_list_elements, mass_operation, doing_simple


# Configure logging
token = 'TOKEN'
logging.basicConfig(level=logging.INFO)
bot = Bot(token='TOKEN')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Этот handler будет вызыван когда пользователь отправит
    команду `/start` или `/help`
    """
    await message.reply(
        f"Привет!\nЯ EchoBot!\nИли напиши выражение,которое хочешь посчитать.")


@dp.message_handler()
async def main(message: types.Message):
    expression: str = message.text
    arr = get_list_elements(expression)
    arr = doing_simple(arr)
    result = mass_operation(arr)
    await message.answer(f'Результат выражения\n{expression}={result}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
