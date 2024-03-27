from button import ImageButton
import pygame
from fade import fade
import sys


def init_main(WIDTH, HEIGHT, file_path_buttons,file_path_music):
    start_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 - 80,
        350,
        74,
        "Играть",
        f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
    )

    settings_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 20,
        350,
        74,
        "Настройки",
        f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
    )

    exit_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 120,
        350,
        74,
        "Выйти",
        f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
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