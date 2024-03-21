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
import time


# импортируем функции из файлов
import page_0_main
import page_1_settings
import page_2_audio
import page_3_video
import page_4_levels
import page_5_storystart
import page_6_game
import page_7_menus
import page_8_recipes
import page_9_pizza



# Инициализация pygame
pygame.init()

# считываем из файла разрешение экрана

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



MAX_FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("котокафе")
main_background = resize_background("src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
game_background = resize_background("src/art/backgrounds/background2.png", WIDTH, HEIGHT)
#pygame.display.set_icon(pygame.image.load("icon.ico"))

clock = pygame.time.Clock()


# загружаем музыкальный файл
pygame.mixer.music.load("src/music/soundtreck.mp3")
# воспроизводим музыку постоянно по кругу
pygame.mixer.music.play(1)
# Загрузка и установка курсора можно поменять на свою картинку, но хз на какую
# cursor = pygame.image.load("Inkedcursor_LI.jpg") #картинка для курсора, сейчас там она прозрачная
pygame.mouse.set_visible(True)  # Скрываем стандартный курсор


PAGE = 0
INIT_MAIN = False
INIT_SETTINGS = False
INIT_AUDIO = False
INIT_VIDEO = False
INIT_LEVELS = False
INIT_STORY_START = False
INIT_GAME = False
INIT_MENUS = False
INIT_RECIPES = False
INIT_PIZZA = False


if (platform.system() == 'Linux'):
    file_path = "./src/art/ingredients/"
else:
    file_path = "\\src\\art\\ingredients\\"


# главное меню и функция
def main_menu():
    global PAGE, INIT_MAIN, INIT_SETTINGS, INIT_AUDIO, INIT_VIDEO, INIT_LEVELS,\
        INIT_STORY_START, INIT_GAME, INIT_MENUS, INIT_RECIPES,INIT_PIZZA, pizza_surface, pizza_rect

    running = True
    WIDTH, HEIGHT = read_size()
    #buttons = page_0_main.init_main(WIDTH, HEIGHT)
    while running:
        screen.fill((0, 0, 0))
        WIDTH, HEIGHT = read_size()
        # """ Главное меню """
        if PAGE == 0 and INIT_MAIN == False:
            background = resize_background("./src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
            buttons = page_0_main.init_main(WIDTH, HEIGHT)
            INIT_MAIN = True

        # """ Окно настройки
        elif PAGE == 1 and INIT_SETTINGS == False:
            INIT_MAIN = False
            background = resize_background("./src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_1_settings.init_settings(WIDTH, HEIGHT)
            INIT_SETTINGS = True

        # """ Окно настройки аудио """
        elif PAGE == 2 and INIT_AUDIO == False:
            INIT_SETTINGS = False
            background = resize_background("./src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_2_audio.init_audio(WIDTH, HEIGHT)
            INIT_AUDIO = True

        # """ Окно настройки видео """
        elif PAGE == 3 and INIT_VIDEO == False:
            INIT_SETTINGS = False
            background = resize_background("./src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_3_video.init_video(WIDTH, HEIGHT)
            INIT_VIDEO = True

        # """ Окно выбора уровня """
        elif PAGE == 4 and INIT_LEVELS == False:
            INIT_MAIN = False
            background = resize_background("./src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_4_levels.init_levels(WIDTH, HEIGHT)
            INIT_LEVELS = True

        # """ Окно история игры  """
        elif PAGE == 5 and INIT_STORY_START == False:
            INIT_LEVELS = False
            background = resize_background("./src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_5_storystart.init_storystart(WIDTH, HEIGHT)
            INIT_STORY_START = True

        # """ Главное окно игры """
        elif PAGE == 6 and INIT_GAME == False:
            INIT_LEVELS = False
            background = resize_background("./src/art/backgrounds/background2.png", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_6_game.init_game(WIDTH, HEIGHT)
            INIT_GAME = True

        # """ Окно меню """
        elif PAGE == 7 and INIT_MENUS == False:
            INIT_GAME = False
            background = resize_background("./src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_7_menus.init_menus(WIDTH, HEIGHT)
            INIT_MENUS = True

        # """ Окно с рецептами """
        elif PAGE == 8 and INIT_RECIPES == False:
            INIT_MENUS = False
            background = resize_background("./src/art/backgrounds/background1.jpg", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_8_recipes.init_recipes(WIDTH, HEIGHT)
            page_8_recipes.recipes_img(WIDTH)
            INIT_RECIPES = True

        # """ Окно приготовления пиццы """
        elif PAGE == 9 and INIT_PIZZA == False:
            INIT_MENUS = False
            background = resize_background("src/art/backgrounds/doska.jpg", WIDTH, HEIGHT)
            screen.blit(background, (0, 0))
            buttons = page_9_pizza.init_pizza(WIDTH, HEIGHT)
            pizza_surface = pygame.Surface((HEIGHT / 2, HEIGHT / 2))
            pizza_surface.fill((0, 0, 0))  # белый цвет
            pizza_surface.set_alpha(200)  # полупрозрачность
            pizza_rect = pizza_surface.get_rect()
            pizza_rect.center = (WIDTH / 2, HEIGHT / 2)  # центр экрана
            page_9_pizza.pizza_img(WIDTH,HEIGHT)
            INIT_PIZZA = True

        screen.blit(background, (0, 0))


        if PAGE == 5 :
            page_5_storystart.story(screen, WIDTH, HEIGHT)
        elif PAGE == 6:
            page_6_game.game(screen, WIDTH, HEIGHT)
        elif PAGE == 8:
            page_8_recipes.recipes(screen, WIDTH, HEIGHT)
        elif PAGE == 9:

            page_9_pizza.pizza(screen,WIDTH,HEIGHT)


        # обработчик конопчек
        for event in pygame.event.get():
            # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if PAGE == 0:
                PAGE = page_0_main.main_handler(event, buttons)

            elif PAGE == 1:
                PAGE = page_1_settings.settings_handler(event, buttons)
                if PAGE == 0:
                    buttons = []
                    INIT_SETTINGS = False
                    break

            elif PAGE == 2:
                PAGE = page_2_audio.audio_handler(screen, event, buttons)
                if PAGE == 1:
                    buttons = []
                    INIT_AUDIO = False
                    break

            elif PAGE == 3:
                PAGE = page_3_video.video_handler(screen, event, buttons)
                if PAGE == 1:
                    buttons = []
                    INIT_VIDEO = False
                    break

            elif PAGE == 4:
                PAGE = page_4_levels.levels_handler(event, buttons)
                if PAGE == 1:
                    buttons = []
                    INIT_LEVELS = False
                    break
                if PAGE == 5:
                    buttons = []
                    INIT_LEVELS = False
                    break

            elif PAGE == 5:
                PAGE = page_5_storystart.story_handler(event, buttons)
                if PAGE == 4:
                    buttons = []
                    INIT_STORY_START = False
                    break

            elif PAGE == 6:
                PAGE = page_6_game.game_handler(event,screen, buttons,WIDTH,HEIGHT)
                if PAGE == 4:
                    buttons = []
                    INIT_GAME = False
                    break

            elif PAGE == 7:
                PAGE = page_7_menus.menus_handler(event, buttons)
                print(PAGE)
                if PAGE == 6:
                    buttons = []
                    INIT_MENUS = False
                    break

            elif PAGE == 8:
                PAGE = page_8_recipes.recipes_handler(event, buttons)
                if PAGE == 7:
                    buttons = []
                    INIT_RECIPES = False
                    break
            elif PAGE == 9:
                PAGE = page_9_pizza.pizza_handler(event, buttons)
                if PAGE == 6 or PAGE == 7:
                    buttons = []
                    INIT_PIZZA = False
                    break
            else:
                pass

            # рисуют и опрашивают кнопчки
            for btn in buttons:
                btn.handle_event(event)

            if PAGE == 9 and INIT_PIZZA == True:
                page_9_pizza.pizza_draw(pizza_surface,event)

        if PAGE == 9 and INIT_PIZZA == True:
            # рисуем поверхность пиццы на экране
            screen.blit(pizza_surface, pizza_rect)


        for btn in buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
        clock.tick(MAX_FPS)

# бесконечный цикл?
if __name__ == "__main__":
    main_menu()

