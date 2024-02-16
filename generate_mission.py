import random
import json
import os


# функция отвечающая за генерацию миссии, пока умеет выбирать слуйчайного героя, текст сюжетный к нему, и количество ингридиентов для пиццы
def generate_mission():
    print("generate_mission")
    # определяем папку, где хранятся картинки
    image_folder = "\\dreamteam\\src\\art\\guest"

    # получаем список всех файлов в папке
    image_files = os.listdir(image_folder)

    # выбираем случайный файл(файфу) из списка
    random_image = random.choice(image_files)

    # выбираем случайное число(сыра) от 1 до 4
    random_cheese = random.randint(0, 4)
    random_tomat = random.randint(0, 4)
    random_dough = random.randint(1, 2)

    # определяем папку, где хранятся текстовые файлы с историей
    text_folder = "\\dreamteam\\src\\txt"

    # получаем список всех файлов в папке
    text_files = os.listdir(text_folder)

    # выбираем случайный файл из списка
    random_text = random.choice(text_files)

    print(random_image)
    print(random_cheese)
    print(random_text)
    file = open("mission.json", "w+")

    # записываем текст в файл
    file.write(
        '{"image":"'
        + str(random_image)
        + '", "random_cheese":'
        + str(random_cheese)
        + ', "text":"'
        + str(random_text)
        + '", "random_tomat":'
        + str(random_tomat)
        + ', "random_dough":'
        + str(random_dough)
        + "}"
    )

    # закрываем файл
    file.close()


    x=0
    file = open("cheese.txt", "w+")
    # записываем текст в файл
    file.write(str(x))
    # закрываем файл
    file.close()


    # в random_number хранится количество пицц, это техническая инфа
    file = open("tomat.txt", "w+")
    # записываем текст в файл
    file.write(str(x))
    # закрываем файл
    file.close()        # в random_number хранится количество пицц, это техническая инфа

    file = open("dough.txt", "w+")
    # записываем текст в файл
    file.write(str(x))
    # закрываем файл
    file.close()









