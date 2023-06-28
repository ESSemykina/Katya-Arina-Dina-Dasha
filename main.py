import json
import os
import requests
from auth_data import token
import vk_api
import vkapi
import api
import time
import datetime

#id_name = input("Введите название группы: ")
#ссылка для доступа к стене в вк
#url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=5&access_token={token}&v=5.131"
#req = requests.get(url)
#print(req.text)
"""vk = vk_api.VkApi(token="vk1.a.VZCTiIKSUiuLOxRA-ljKghO0fKVOIB7dvxvtLJ9rQ8GlKjVTJg7jn2XhA3ucwhgnYjKCVf5EdPEBgKNQ-wfWdTavYvWPU5kiu9U0uHBzJBVh7Kx6jUCEtPTUo_Du26sQSHMCYt2349usjVQ36XYrcOWJp7uSWestxyjqnz-keku3exosRCJCscRalKGNcE3So3mUudL4mjlmaaGZ-NqFeA")
def getProfileInfo(id_name):
    # получение имени и фамилии
    user = vk.method("users.get", {"user_ids": id_name})
    name = user[0]['first_name']
    surname = user[0]['last_name']

    print("Имя:",name,"\nФамилия:",surname)"""


def get_user_data(id_name):
    # Ваш access token VK API
    access_token = "vk1.a.VZCTiIKSUiuLOxRA-ljKghO0fKVOIB7dvxvtLJ9rQ8GlKjVTJg7jn2XhA3ucwhgnYjKCVf5EdPEBgKNQ-wfWdTavYvWPU5kiu9U0uHBzJBVh7Kx6jUCEtPTUo_Du26sQSHMCYt2349usjVQ36XYrcOWJp7uSWestxyjqnz-keku3exosRCJCscRalKGNcE3So3mUudL4mjlmaaGZ-NqFeA"

    # Параметры запроса
    params = {
        'user_ids': id_name,
        'fields': 'first_name,last_name,city,country,sex',
        'access_token': access_token,
        'v': '5.131'
    }

    # URL для запроса к VK API
    url = 'https://api.vk.com/method/users.get'

    try:
        response = requests.get(url, params=params)
        data = response.json()


        # Вывод данных пользователя в формате JSON
        print(data)


    except Exception as e:
        print('Произошла ошибка:', e)



def main():
    id_name = input("Введите название группы: ")
    #get_wall_posts(id_name)


    # Пример использования функции
    get_user_data(id_name)
    #getProfileInfo(id_name)


if __name__ == '__main__':
    main()
