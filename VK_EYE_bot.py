import requests
from auth_data import token_bot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=token_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Введи ФИО человека или ссылку на страницу VK")

if __name__ == '__main__':
    executor.start_polling(dp)