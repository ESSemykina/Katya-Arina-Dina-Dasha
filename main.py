import json
import os
import requests
from auth_data import token

#group_name = input("Введите название группы: ")
#ссылка для доступа к стене в вк
#url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=5&access_token={token}&v=5.131"
#req = requests.get(url)
#print(req.text)

def get_wall_posts(group_name):
    #ссылка для доступа к стене в вк
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=5&access_token={token}&v=5.131"
    req = requests.get(url)
    #сохраняем полученные данные в src
    src = req.json()

    # проверяем существует ли директория с именем группы
    if os.path.exists(f"{group_name}"):
        print(f"Директория с именем {group_name} уже существует!")
    else:
        os.mkdir(group_name)

    # сохраняем данные в json файл, чтобы видеть структуру
    with open(f"{group_name}/{group_name}.json", "w", encoding="utf-8") as file:
        json.dump(src, file, indent=4, ensure_ascii=False)


    # собираем ID новых постов в список
    fresh_posts_id = []
    posts = src["response"]["items"]

    #достаём айди каждого поста,обращаясь к ключу айди на каждой итерации пополняем наш список
    for fresh_post_id in posts:
        fresh_post_id = fresh_post_id["id"]
        fresh_posts_id.append(fresh_post_id)

    """Проверка, если файла не существует, значит это первый
       парсинг группы(отправляем все новые посты). Иначе начинаем
       проверку и отправляем только новые посты."""

    if not os.path.exists(f"{group_name}/exist_posts_{group_name}.txt"):
        print("Файла с ID постов не существует, создаём файл!")
        #открываем файл на запись
        with open(f"{group_name}/exist_posts_{group_name}.txt", "w") as file:
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
        print("Файл с ID постов найден, начинаем выборку  свежих постов!")

def main():
    group_name = input("Введите название группы: ")
    get_wall_posts(group_name)


if __name__ == '__main__':
    main()