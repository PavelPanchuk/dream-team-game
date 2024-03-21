from button import ImageButton
import pygame
from fade import fade
import sys


def init_main(WIDTH, HEIGHT):
    start_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 - 80,
        350,
        74,
        "Играть",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )

    settings_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 20,
        350,
        74,
        "Настройки",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )

    exit_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 120,
        350,
        74,
        "Выйти",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    return [start_button, settings_button, exit_button]


def main_handler(event,buttons):
    global INIT_MAIN
    start_button, settings_button, exit_button = buttons
    if event.type == pygame.USEREVENT and event.button == start_button:
        fade()
        # переход на страницу "УРОВНИ"
        page = 4
        return page

    elif event.type == pygame.USEREVENT and event.button == settings_button:
        fade()
        # переход на страницу "НАСТРОЙКИ"
        page = 1
        return page

    elif event.type == pygame.USEREVENT and event.button == exit_button:
        pygame.quit()
        sys.exit()
    else:
        return 0