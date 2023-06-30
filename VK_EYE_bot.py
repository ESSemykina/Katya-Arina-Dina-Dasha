import requests
import os
import json
from aiogram.types import ContentTypes, ContentType, Message
from auth_data import token_bot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from PIL import Image
import emoji
import vk_api

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
            'fields': 'first_name,last_name,city,country,sex,relation,bdate,universities,status_info,photo_200',
            'access_token': access_token,
            'v': '5.131'
        }
        # URL для запроса к VK API
        url = 'https://api.vk.com/method/users.get'
        response = requests.get(url, params=params)
        data = response.json()


        # Check if the directory with the user's ID already exists
        id_name = str(data["response"][0]["id"])
        if os.path.exists(id_name):
            print("", end="")
        else:
            os.mkdir(id_name)

        # Save the user's data in a JSON file for better visualization of the structure
        with open(f"{id_name}/{id_name}.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        user_info = data["response"][0]

        first_name = user_info.get("first_name", "Не указано")
        last_name = user_info.get("last_name", "Не указана")
        bdate = user_info.get("bdate", "Не указана")
        gender = user_info.get("sex")
        relation = user_info.get("relation")
        city = user_info.get("city", {}).get("title", "Не указан")
        country = user_info.get("country", {}).get("title", "Не указана")
        universities = user_info.get("universities", [])
        photo_url = user_info.get("photo_200")
        # Запрос к API ВКонтакте
        response = requests.get(
            f"https://api.vk.com/method/users.get?user_ids={id_name}&fields=status&access_token={access_token}&v=5.131")

        # Получение статуса пользователя
        status = response.json()["response"][0]["status"]
        # Запрос к API ВКонтакте


        if gender == 1:
            gender = "Женский"
        elif gender == 2:
            gender = "Мужской"
        else:
            gender = "Не указан"

        if relation == 1:
            relation = "Не женат/Не замужем"
        if relation == 2:
            relation = "Есть друг/ подруга"
        if relation == 3:
            relation = "Помолвлен(а)"
        if relation == 4:
            relation = "Женат/Замужем"
        if relation == 5:
            relation = "Всё сложно"
        if relation == 6:
            relation = "В активном поиске"
        if relation == 7:
            relation = "Влюблен(а)"
        if relation == 8:
            relation = "В гражданском браке"
        if relation == 0:
            relation = "Не указано"

        education_info = ""
        if universities:
            for item in universities:
                university_name = item.get("name", "Не указано")
                graduation_year = item.get("graduation", "Не указан")
                education_info += f" {university_name}\n" \
                                  f"Год окончания: {graduation_year}"

        # Проверка наличия эмодзи в статусе и вывод настроения
        status_info= ""

        if   "😀" in status or "😃" in status or "😄" in status or "😁" in status or "😇" in status or "🙂" in status:
            status_info = "Пользователь счастлив"
        elif "😒" in status or "😞" in status or "😔"in status or "😟" in status or "☹️" in status or  "😣" in status or "😖"  in status:
            status_info = "Пользователь грустит"
        elif "🤮 " in status or "🤧" in status  or "😷" in status or "🤒" in status or "🤕" in status:
            status_info = "Пользователь болеет"
        elif "😠"  in status or "😡" in status  or "🤬" in status:
            status_info = "Пользователь зол"
        elif "😎"  in status:
            status_info = "Пользователь крут"
        elif "😴" in status or "🥱 "  in status:
            status_info = "Пользователь любит поспать"
        elif "😢" in status or "😭" in status or "😰" in status or "😓" in status:
            status_info = "Пользователь плачет"
        elif "❤️" in status  or " 😘" in status or "😍" in status or "💋" in status or "😚" in status or "🥰" in status:
            status_info = "У пользователя любовное настроение"
        else:
            status_info = "У пользователя нейтральное настроение"



        await message.answer(
            f"Имя пользователя: {first_name}\n"
            f"Фамилия пользователя: {last_name}\n"
            f"Дата рождения: {bdate}\n"
            f"Пол: {gender}\n"
            f"Семейное положение: {relation}\n"
            f"Город: {city}\n"
            f"Страна: {country}\n"
            f"Место учебы:{education_info}\n"
            f"Статус пользователя:{status_info}\n"
            f"{photo_url}"


        )
        # Вывод данных пользователя в формате JSON
        # print(data)


    except Exception as e:
        await message.reply('Произошла ошибка: ' + str(e))




if __name__ == '__main__':
    executor.start_polling(dp)
