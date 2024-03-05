
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
from fade import fade

#from main import new_game




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


def resize_background(filename, width, height):
    background = pygame.image.load(filename)
    background = pygame.transform.scale(background, (width, height))
    return background



MAX_FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("котокафе")
main_background = resize_background("background1.jpg", WIDTH, HEIGHT)
game_background = resize_background("background2.jpg", WIDTH, HEIGHT)
pygame.display.set_icon(pygame.image.load("icon.ico"))

clock = pygame.time.Clock()













# функция настроек
def storystart():
    WIDTH, HEIGHT = read_size()
    # Создание кнопок
    continue_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 148,
        252,
        74,
        "Окей, помогу!",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
   
    running = True
    while running:
        screen.fill((0, 0, 0))
        background = resize_background("background2.jpg", WIDTH, HEIGHT)
        screen.blit(background, (0, 0))
        random_image="ba.png"
        random_text="storystart.txt"


        # Загрузка изображения  выбранной вайфу
        if (platform.system() == 'Linux'):
            image =  pygame.image.load("./src/story/person/" + random_image)
            file_path = "./src/story/txt/" + random_text
        else:
            file_path =(random_text)
            image = pygame.image.load(random_image)
            #file_path =("\\dream-team-game-dev\\src\\story\\txt\\" + random_text)
            #image = pygame.image.load("\\dream-team-game-dev\\src\\story\\person\\" + random_image)

        # number= pygame.text.load()



        # открываем файл для чтения
        file = open(file_path, "r", encoding="utf-8")

        # читаем текст из файла и записываем его в переменную
        text = file.read()

        # закрываем файл
        file.close()
        # выводим текст на экран
        # print(text)




        '''
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)
        '''
        # Координаты для размещения изображения
        
        x = 100
        y = 200
        width, height = image.get_size()




        # Уменьшение размера изображения в два раза
        image = pygame.transform.scale(image, (width // 5, height // 2))
        # Размещение изображения на экране
        screen.blit(image, (x, y))



        font = pygame.font.Font(None, 72)
        text_surface = font.render(str(text), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == continue_button:
                print("Кнопка 'продолжить' была нажата!")


                fade()
                running = False
                return

            for btn in [continue_button]:
                btn.handle_event(event)

        for btn in [continue_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)


        pygame.display.flip()
        clock.tick(MAX_FPS)