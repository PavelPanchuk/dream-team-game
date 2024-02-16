

import random
import json
import os



#функция отвечающая за генерацию миссии, пока умеет выбирать слуйчайного героя, текст сюжетный к нему, и количество пицц
def generate_mission():
    # определяем папку, где хранятся картинки
    image_folder = "\\dreamteam\\src\\art\\guest"

    # получаем список всех файлов в папке
    image_files = os.listdir(image_folder)

    # выбираем случайный файл(файфу) из списка
    random_image = random.choice(image_files)

    # выбираем случайное число(пицц) от 1 до 4
    random_number = random.randint(1, 4)

    # определяем папку, где хранятся текстовые файлы с историей
    text_folder = "\\dreamteam\\src\\txt"

    # получаем список всех файлов в папке
    text_files = os.listdir(text_folder)

    # выбираем случайный файл из списка
    random_text = random.choice(text_files)

    print(random_image)
    print(random_number)
    print(random_text)
    file = open('mission.json', 'w+')

                # записываем текст в файл
    file.write('{"image":"'+ str(random_image)+'", "number":'+str(random_number)+',"text":"'+str(random_text)+'"}')

                # закрываем файл
    file.close()

    #в random_number хранится количество пицц, это техническая инфа
    file = open('mission_teh.txt', 'w+')

                # записываем текст в файл
    file.write(str(random_number))

                # закрываем файл
    file.close()
    









