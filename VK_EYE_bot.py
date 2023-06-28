import requests
import os
import json
from auth_data import token_bot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=token_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Введи id пользователя VK")


@dp.message_handler()
async def get_user_data(message: types.Message):
    access_token = "vk1.a.VZCTiIKSUiuLOxRA-ljKghO0fKVOIB7dvxvtLJ9rQ8GlKjVTJg7jn2XhA3ucwhgnYjKCVf5EdPEBgKNQ-wfWdTavYvWPU5kiu9U0uHBzJBVh7Kx6jUCEtPTUo_Du26sQSHMCYt2349usjVQ36XYrcOWJp7uSWestxyjqnz-keku3exosRCJCscRalKGNcE3So3mUudL4mjlmaaGZ-NqFeA"

    try:
        id_name = message.text

        params = {
            'user_ids': id_name,
            'fields': 'first_name,last_name,city,country,sex,bdate',
            'access_token': access_token,
            'v': '5.131'
        }
        # URL для запроса к VK API
        url = 'https://api.vk.com/method/users.get'
        response = requests.get(url, params=params)
        data = response.json()

        # проверяем существует ли директория с id пользователя
        if os.path.exists(f"{id_name}"):
            print("", end="")
        else:
            os.mkdir(id_name)
        # сохраняем данные в json файл, чтобы видеть структуру
        with open(f"{id_name}/{id_name}.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        user_info = data["response"][0]

        first_name = user_info.get("first_name", "Не указано")
        last_name = user_info.get("last_name", "Не указана")
        bdate = user_info.get("bdate", "Не указана")
        gender = user_info.get("sex")
        city = user_info.get("city", {}).get("title", "Не указан")
        country = user_info.get("country", {}).get("title", "Не указана")

        if gender == 1:
            gender = "Женский"
        elif gender == 2:
            gender = "Мужской"
        else:
            gender = "Не указан"

        await message.answer(
            f"Имя пользователя: {first_name}\n"
            f"Фамилия пользователя: {last_name}\n"
            f"Дата рождения: {bdate}\n"
            f"Пол: {gender}\n"
            f"Город: {city}\n"
            f"Страна: {country}"
        )
        # Вывод данных пользователя в формате JSON
        # print(data)


    except Exception as e:
        await message.reply('Произошла ошибка: ' + str(e))


if __name__ == '__main__':
    executor.start_polling(dp)
