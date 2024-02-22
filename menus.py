import pygame
import sys
from button import ImageButton
import json


from pizza_window import pizza_window
from spice_window import spice_window

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

WIDTH, HEIGHT = read_size()

def resize_background(filename, width, height):
    background = pygame.image.load(filename)
    background = pygame.transform.scale(background, (width, height))
    return background


MAX_FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("котокафе")
main_background = resize_background("background1.jpg", WIDTH, HEIGHT)
pygame.display.set_icon(pygame.image.load("icon.ico"))

clock = pygame.time.Clock()


# Загрузка и установка курсора можно поменять на свою картинку, но хз на какую
cursor = pygame.image.load("cursor.png")
pygame.mouse.set_visible(True)  # Скрываем стандартный курсор
# затемнение
def fade():
    running = True
    fade_alpha = 0  # Уровень прозрачности для анимации

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
        clock.tick(30)  # Ограничение FPS


def menus():
    WIDTH, HEIGHT = read_size()
    print("menu def")
    # Создание кнопок
    spice_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 148,
        252,
        74,
        "Рецепты",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
    pizza_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 48,
        252,
        74,
        "к готовке пиццы",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
    back_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 + 52,
        252,
        74,
        "к заказу",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )
#обработчик событий(кнопок)
    running = True
    while running:
        screen.fill((0, 0, 0))
        background = resize_background("background1.jpg", WIDTH, HEIGHT)
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Управление кафе", True, (255, 255, 255))
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

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            if event.type == pygame.USEREVENT and event.button == spice_button:
                fade()
                running = False
                spice_window()

            if event.type == pygame.USEREVENT and event.button == pizza_button:
                fade()
                running = False
                pizza_window()

            for btn in [spice_button, pizza_button, back_button]:
                btn.handle_event(event)

        for btn in [spice_button, pizza_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()
