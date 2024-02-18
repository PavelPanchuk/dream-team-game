
import pygame
import sys
from button import ImageButton
import pygame_menu
import json


# Инициализация pygame
pygame.init()

def read_size():
    file = open("settings.json", "r")
    data = json.loads(file.read())

    # Параметры экрана

    width = data["WIDTH"]
    height = data["HEIGHT"]
    file.close()
    return width, height

def resize_background(filename, width, height):
    background = pygame.image.load(filename)
    background = pygame.transform.scale(background, (width, height))
    return background

WIDTH, HEIGHT = read_size()

MAX_FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("video settings")
main_background = resize_background("background1.jpg", WIDTH, HEIGHT)


clock = pygame.time.Clock()





# Загрузка и установка курсора можно поменять на свою картинку, но хз на какую
cursor = pygame.image.load("cursor.png") 
pygame.mouse.set_visible(True)  # Скрываем стандартный курсор
# затемнение
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

def settings_video_menu():
    print("video settings")
    WIDTH, HEIGHT = read_size()
        # Создание кнопок
    # Создание кнопок
    low_button = ImageButton(WIDTH / 2 - (252 / 2), HEIGHT / 2 - 148, 252, 74, "960x600", "green_button2.jpg",
                             "green_button2_hover.jpg", "click.mp3")
    full_button = ImageButton(WIDTH / 2 - (252 / 2), HEIGHT / 2 - 48, 252, 74, "1280x640", "green_button2.jpg",
                              "green_button2_hover.jpg", "click.mp3")
    hd_button = ImageButton(WIDTH / 2 - (252 / 2), HEIGHT / 2 + 52, 252, 74, "1920x1080", "green_button2.jpg",
                            "green_button2_hover.jpg", "click.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), HEIGHT / 2 + 152, 252, 74, "Назад", "green_button2.jpg",
                              "green_button2_hover.jpg", "click.mp3")


    running = True
    while running:
        screen.fill((0, 0, 0))
        background = resize_background("background1.jpg", WIDTH, HEIGHT)
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Изменить разрешение экрана", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2,100))
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

            if event.type == pygame.USEREVENT and event.button == hd_button:
                file = open('settings.json', 'w+')

                # записываем текст в файл
                file.write('{"WIDTH": 1920, "HEIGHT": 1080,"MAX_FPS":60}')

                # закрываем файл
                file.close()
            if event.type == pygame.USEREVENT and event.button == full_button:
                file = open('settings.json', 'w+')

                # записываем текст в файл
                file.write('{"WIDTH": 1280, "HEIGHT": 1024,"MAX_FPS":60}')

                # закрываем файл
                file.close()

            if event.type == pygame.USEREVENT and event.button == low_button:
                file = open('settings.json', 'w+')

                # записываем текст в файл
                file.write('{"WIDTH": 960, "HEIGHT": 600,"MAX_FPS":60}')

                # закрываем файл
                file.close()
                # добавляем виджет селектора в меню


            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [low_button, back_button,full_button,hd_button]:
                btn.handle_event(event)

        for btn in [ low_button, back_button,full_button,hd_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()
#меню готовка кухня короче

