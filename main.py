import json
import os
import requests
from auth_data import token
import vk_api
import vkapi
import api


#id_name = input("Введите название группы: ")
#ссылка для доступа к стене в вк
#url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=5&access_token={token}&v=5.131"
#req = requests.get(url)
#print(req.text)
vk = vk_api.VkApi(token="vk1.a.VZCTiIKSUiuLOxRA-ljKghO0fKVOIB7dvxvtLJ9rQ8GlKjVTJg7jn2XhA3ucwhgnYjKCVf5EdPEBgKNQ-wfWdTavYvWPU5kiu9U0uHBzJBVh7Kx6jUCEtPTUo_Du26sQSHMCYt2349usjVQ36XYrcOWJp7uSWestxyjqnz-keku3exosRCJCscRalKGNcE3So3mUudL4mjlmaaGZ-NqFeA")
def getProfileInfo(id_name):
    # получение имени и фамилии
    user = vk.method("users.get", {"user_ids": id_name})
    name = user[0]['first_name']
    surname = user[0]['last_name']
    print("Имя:",name,"\nФамилия:",surname)

"""def get_wall_posts(id_name):
    #ссылка для доступа к стене в вк
    url = f"https://api.vk.com/method/wall.get?domain={id_name}&count=5&access_token={token}&v=5.131"
    req = requests.get(url)
    #сохраняем полученные данные в src
    src = req.json()

    # проверяем существует ли директория с именем группы
    if os.path.exists(f"{id_name}"):
        print(f"Директория с именем {id_name} уже существует!")
    else:
        os.mkdir(id_name)

    # сохраняем данные в json файл, чтобы видеть структуру
    with open(f"{id_name}/{id_name}.json", "w", encoding="utf-8") as file:
        json.dump(src, file, indent=4, ensure_ascii=False)


    # собираем ID новых постов в список
    fresh_posts_id = []
    posts = src["response"]["items"]

    #достаём айди каждого поста,обращаясь к ключу айди на каждой итерации пополняем наш список
    for fresh_post_id in posts:
        fresh_post_id = fresh_post_id["id"]
        fresh_posts_id.append(fresh_post_id)

   # Проверка, если файла не существует, значит это первый
    #   парсинг группы(отправляем все новые посты). Иначе начинаем
     #  проверку и отправляем только новые посты.

    if not os.path.exists(f"{id_name}/exist_posts_{id_name}.txt"):
        print("Файла с ID постов не существует, создаём файл!")
        #открываем файл на запись
        with open(f"{id_name}/exist_posts_{id_name}.txt", "w") as file:
            for item in fresh_posts_id:   #пробегаемся по списку с айдишниками
                file.write(str(item) + "\n")   # записываем айди с новой строки(str-тк целое получаем целое число)

        # извлекаем данные из постов
        for post in posts:#  пробегаемся по списку
            try:
                if "attachments" in post:# фото и видео лежат в словаре attachments
                    post = post["attachments"]# забираем блок кода в котором содержится ссылки на фотографии
            except Exception:
                print(f"Что-то пошло не так ")

    else:
        print("Файл с ID постов найден, начинаем выборку  свежих постов!")"""

def main():
    id_name = input("Введите название группы: ")
    #get_wall_posts(id_name)

    getProfileInfo(id_name)


if __name__ == '__main__':
    main()
