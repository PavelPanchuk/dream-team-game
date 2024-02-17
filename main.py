# -*- coding: utf-8 -*-
# библиотеки

import random
import pygame
import sys
import json
import os
from pygame import mixer
import shutil
import platform


# импортируем функции из файлов
from button import ImageButton
from menus import menus
from settings_video_menu import settings_video_menu
from settings_audio_menu import settings_audio_menu
from generate_mission import generate_mission


# Инициализация pygame
pygame.init()

# хрень в которой считываем из файла разрешение экрана

def read_size():
    file = open("settings.json", "r")
    data = json.loads(file.read())

    # Параметры экрана

    width = data["WIDTH"]
    height = data["HEIGHT"]
    file.close()
    return width, height

WIDTH, HEIGHT = read_size()

MAX_FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("котокафе")
main_background = pygame.image.load("background1.jpg")
main_background = pygame.transform.scale(main_background, (WIDTH, HEIGHT))
game_background = pygame.image.load("background2.jpg")
game_background = pygame.transform.scale(game_background, (WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load("icon.ico"))

clock = pygame.time.Clock()


# загружаем музыкальный файл
pygame.mixer.music.load("soundtreck.mp3")
# воспроизводим музыку постоянно по кругу
pygame.mixer.music.play(1)
# Загрузка и установка курсора можно поменять на свою картинку, но хз на какую
# cursor = pygame.image.load("Inkedcursor_LI.jpg") #картинка для курсора, сейчас там она прозрачная
pygame.mouse.set_visible(True)  # Скрываем стандартный курсор


# главное меню и функция
def main_menu():
    WIDTH, HEIGHT = read_size()
    # Создание кнопок
    start_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 148,
        252,
        74,
        "Играть",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
    settings_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 48,
        252,
        74,
        "Настройки",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
    exit_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 + 52,
        252,
        74,
        "Выйти",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )

    running = True
    while running:
        screen.fill((0, 0, 0))


        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("MENU TEST", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        # обработчик конопчек
        for event in pygame.event.get():
            # выход
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                print("Кнопка 'Старт' была нажата!")
                fade()
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                print("Кнопка 'Настройки' была нажата!")
                fade()
                settings_menu()
            # тоже выход

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()
            # рисуют и опрашивают кнопчки
            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)
        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        # screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()


# функция настроек
def settings_menu():
    WIDTH, HEIGHT = read_size()
    # Создание кнопок
    audio_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 148,
        252,
        74,
        "Аудио",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
    video_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 48,
        252,
        74,
        "Видео",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
    back_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 + 52,
        252,
        74,
        "Назад",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == video_button:
                print("Кнопка 'Настройки видео' была нажата!")
                fade()
                settings_video_menu()

            if event.type == pygame.USEREVENT and event.button == audio_button:
                print("Кнопка 'Настройки аудио' была нажата!")
                fade()
                settings_audio_menu()

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        # screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()


# функция для запуска самой игры(геймплея)
def new_game():
    WIDTH, HEIGHT = read_size()
    # Создание кнопок
    back_button = ImageButton(
        WIDTH - 1000,
        HEIGHT - 600,
        150,
        74,
        "меню",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
    menus_button = ImageButton(
        WIDTH - 400,
        HEIGHT - 100,
        252,
        74,
        "на кухню",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
    put_button = ImageButton(
        WIDTH - 400,
        HEIGHT - 400,
        252,
        74,
        "отдать заказ",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )

    running = True
    while running:

        screen.fill((0, 0, 0))
        screen.blit(game_background, (0, 0))

        file_path = "money.txt"
        file = open(file_path, "r")
        # читаем число из файла и преобразуем его в целое
        num = int(file.read())
        # закрываем файл
        file.close()
        # проверяем существование файла
        file_path = "day.txt"

                    # задаем другую переменную для сложения

                    # открываем файл для чтения
        file = open(file_path, "r")

                    # читаем число из файла и преобразуем его в целое
        day = int(file.read())

        file.close()

        font = pygame.font.Font(None, 72)
        text_surface = font.render("$" + str(num)+" day "+str(day), True, (0, 255, 255), (255, 204, 153))
        text_rect = text_surface.get_rect(center=(WIDTH / 10, HEIGHT / 20 + 100))
        screen.blit(text_surface, text_rect)



        # тут должно быть что то что генерировало случайного перса и текст с заданием
        file_path = "mission.json"

        # проверяем существование файла
        if (os.path.exists(file_path) and os.path.isfile(file_path))==False:
            
            print("Файл не существует2")
            generate_mission()

            file_path = "hours.txt"

                    # задаем другую переменную для сложения
            other_var = random.randint(1, 5)

                    # открываем файл для чтения
            file = open(file_path, "r")

                    # читаем число из файла и преобразуем его в целое
            num = int(file.read())

                    # закрываем файл
            file.close()

                    # нынешняя сумма + доходы-расходы фактические (тут можно отдать больше товаров чем просят, и это не оплачивается)
            result = int(num) + int(other_var) 
            print(result)
            print(num)
            print(other_var)
            if result>=24:
                result=0
                file_path1 = "day.txt"

                        # задаем другую переменную для сложения
                        # открываем файл для чтения
                file1 = open(file_path1, "r")

                        # читаем число из файла и преобразуем его в целое
                daynow = int(file1.read())

                        # закрываем файл
                file1.close()

                        # открываем файл для записи
                file1 = open(file_path1, "w")
                z=daynow+1
                print("z")
                print(z)
                        # записываем результат в файл, преобразовав его в строку
                file1.write(str(z))

                        # закрываем файл
                file1.close()



                    # открываем файл для записи
            file = open(file_path, "w")

                    # записываем результат в файл, преобразовав его в строку
            file.write(str(result))

                    # закрываем файл
            file.close()






        #получение инфы о миссии
        file = open("mission.json", "r")
        # читаем содержимое файла и преобразуем его в словарь
        data = json.loads(file.read())

        # получаем значение по ключу 'WIDTH' и присваиваем его переменной x
        random_image = data["image"]
        random_cheese = data["random_cheese"]
        random_cheese = str(random_cheese)
        random_tomat = data["random_tomat"]
        random_tomat = str(random_tomat)
        random_dough = data["random_dough"]
        random_dough = str(random_dough)
        random_text = data["text"]
        file.close()


        # Загрузка изображения  выбранной вайфу
        if (platform.system() == 'Linux'):
            image =  pygame.image.load("./src/art/guest/" + random_image)
            file_path = "./src/txt/" + random_text
        else:
            image = pygame.image.load("\\dreamteam\\src\\art\\guest\\" + random_image)
            file_path = "\\dreamteam\\src\\txt\\" + random_text
        # number= pygame.text.load()



        # открываем файл для чтения
        file = open(file_path, "r", encoding="utf-8")

        # читаем текст из файла и записываем его в переменную
        text = file.read()

        # закрываем файл
        file.close()
        # выводим текст на экран
        # print(text)

        font = pygame.font.Font(None, 30)
        text_surface = font.render(
            text +"сыра:"+random_cheese+"помидоров:"+random_tomat+"теста:"+random_dough,
              True,
                (0, 0, 0),
                  (255, 204, 153)
        )
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)
        # Координаты для размещения изображения
        x = 100
        y = 200
        width, height = image.get_size()

        # Уменьшение размера изображения в два раза
        image = pygame.transform.scale(image, (width // 5, height // 2))
        # Размещение изображения на экране
        screen.blit(image, (x, y))

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        # screen.blit(cursor, (x-2, y-2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Возврат в меню
            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
            # вызывается файл с функцией меню
            if event.type == pygame.USEREVENT and event.button == menus_button:
                fade()
                menus()
            # хрень при нажатие на которую можно отдать заказ, сравнивает миссию и что получилось
            if event.type == pygame.USEREVENT and event.button == put_button:
                # задаем путь к папке
                #получение инфы о миссии
                file = open("mission.json", "r")
                data = json.loads(file.read())
                random_cheese = data["random_cheese"]
                random_cheese = int(random_cheese)
                random_tomat = data["random_tomat"]
                random_tomat = int(random_tomat)
                random_dough = data["random_dough"]
                random_dough = int(random_dough)
                file.close()


                file_path = "cheese.txt"
                file = open(file_path, "r")
                need_cheese = int(file.read())
                file.close()
                file_path = "tomat.txt"
                file = open(file_path, "r")
                need_tomat = int(file.read())
                file.close()
                file_path = "dough.txt"
                file = open(file_path, "r")
                need_dough = int(file.read())
                file.close()






                print(random_cheese)                
                print(need_cheese)               
                print(random_tomat)               
                print(need_tomat)                
                print(random_dough)
                print(need_dough)


                if str(random_cheese)<=str(need_cheese) and str(random_tomat)<=str(need_tomat) and str(random_dough)<=str(need_dough):
                    print(f"1 k 1 можно отдать заказ")

                    file_path = "money.txt"

                    # задаем другую переменную для сложения
                    other_var = int(random_cheese) * 200

                    # открываем файл для чтения
                    file = open(file_path, "r")

                    # читаем число из файла и преобразуем его в целое
                    num = int(file.read())

                    # закрываем файл
                    file.close()

                    # нынешняя сумма + доходы-расходы фактические (тут можно отдать больше товаров чем просят, и это не оплачивается)
                    result = int(num) + int(other_var) - 150
                    print(result)
                    print(num)
                    print(other_var)

                    # открываем файл для записи
                    file = open(file_path, "w")

                    # записываем результат в файл, преобразовав его в строку
                    file.write(str(result))

                    # закрываем файл
                    file.close()

                    # задаем путь к файлу
                    file_path = "mission.json"
                    # удаляем файл
                    os.remove(file_path)

                    # задаем путь к директории
                    dir_path = "\\dreamteam\\src\\mission\\pizza\\"

                    # удаляем директорию и все ее содержимое
                    shutil.rmtree(dir_path)
                    # задаем путь к директории
                    dir_path = "\\dreamteam\\src\\mission\\pizza"

                    # создаем директорию
                    os.mkdir(dir_path)


                    file_path = "tomat.txt"

                    # удаляем файл
                    os.remove(file_path)
                    file_path = "cheese.txt"

                    # удаляем файл
                    os.remove(file_path)

                    file_path = "dough.txt"
                    # удаляем файл
                    os.remove(file_path)


                else:
                    font = pygame.font.Font(None, 72)
                    text_surface = font.render(
                        "ТУТ НЕ ВЕСЬ ЗАКАЗ", True, (0, 0, 0), (255, 204, 153)
                    )
                    text_rect = text_surface.get_rect(
                        center=(WIDTH / 10 + 100, HEIGHT / 20 + 300)
                    )
                    screen.blit(text_surface, text_rect)
                    mixer.init()

                    # загружаем файл с музыкой
                    mixer.music.load("error.mp3")

                    # воспроизводим музыку бесконечно с начала
                    mixer.music.play(0, 0.0)
                    pygame.mixer.music.load("soundtreck.mp3")

                    # воспроизводим музыку постоянно по кругу
                    pygame.mixer.music.play(1)

                print(random_cheese)

            # cюда вставлять кнопочки для отрисовочки очка
            for btn in [back_button, menus_button, put_button]:
                btn.handle_event(event)
        # cюда вставлять кнопочки для отрисовочки очка
        for btn in [back_button, menus_button, put_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


# затемнение при переходе между экранами, для красоты
def fade():
    running = True
    fade_alpha = 0  # Уровень прозрачности для анимации
    WIDTH, HEIGHT = read_size()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Анимация затухания текущего экрана
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        # Увеличение уровня прозрачности
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)  # Ограничение FPS


# бесконечный цикл?
if __name__ == "__main__":
    main_menu()
