import json
import os
import requests

from auth_data import token


def get_user_data(id_name):

    access_token = "vk1.a.VZCTiIKSUiuLOxRA-ljKghO0fKVOIB7dvxvtLJ9rQ8GlKjVTJg7jn2XhA3ucwhgnYjKCVf5EdPEBgKNQ-wfWdTavYvWPU5kiu9U0uHBzJBVh7Kx6jUCEtPTUo_Du26sQSHMCYt2349usjVQ36XYrcOWJp7uSWestxyjqnz-keku3exosRCJCscRalKGNcE3So3mUudL4mjlmaaGZ-NqFeA"

    # Параметры запроса
    params = {
        'user_ids': id_name,
        'fields': 'first_name,last_name,city,country,sex,relation,bdate,education,career,photo_200',
        'access_token': access_token,
        'v': '5.131'
    }
    api_version = "5.131"
    # URL для запроса к VK API
    url = f"https://api.vk.com/method/users.get?user_ids={id_name}&fields=education,career&access_token={access_token}&v={api_version}"




    try:
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
       # id_name = user_info.get("id")

        first_name = user_info.get("first_name", "Не указано")
        last_name = user_info.get("last_name", "Не указана")
        bdate = user_info.get("bdate", "Не указана")
        gender = user_info.get("sex")
        relation = user_info.get("relation")
        city = user_info.get("city", {}).get("title", "Не указан")
        country = user_info.get("country", {}).get("title", "Не указана")
        education = user_info.get("education")
        career = user_info.get("career")

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
        if education:
            for item in education:
                school_name = item.get("name", "Не указано")
                graduation_year = item.get("graduation", "Не указан")
                education_info += f"Учебное заведение: {school_name}\n" \
                                  f"Год окончания: {graduation_year}\n\n"

        career_info = ""
        if career:
            for item in career:
                company_name = item.get("company", "Не указано")
                position = item.get("position", "Не указана")
                career_info += f"Место работы: {company_name}\n" \
                               f"Должность: {position}\n\n"
        print("Имя пользователя:", first_name)
        print("Фамилия пользователя:", last_name)
        print("Дата рождения:",bdate)
        print("Пол:", gender)
        print("Семейное положение:", relation)
        print("Город:", city)
        print("Страна:", country)
        print("Место учебы:", education_info)
        print("Место работы:", career_info)

        # Вывод данных пользователя в формате JSON
        #print(data)


    except Exception as e:
        print('Произошла ошибка:', e)



def main():
    id_name = input("Введите id пользователя: ")
    get_user_data(id_name)

if __name__ == '__main__':
    main()
