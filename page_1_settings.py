from button import ImageButton
import pygame
from fade import fade
import sys
import main

def init_settings(WIDTH, HEIGHT):
    audio_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 - 80,
        400,
        74,
        "Аудио",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    video_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 20,
        400,
        74,
        "Видео",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    back_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 120,
        400,
        74,
        "Назад",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    return [audio_button, video_button, back_button]


def settings_handler(event, buttons):
    global INIT_MAIN
    audio_button, video_button, back_button = buttons
    if event.type == pygame.USEREVENT and event.button == video_button:
        print("Кнопка 'Настройки видео' была нажата!")
        fade()
        # переход на страницу "НАСТРОЙКИ ВИДЕО"
        page = 3
        return page

    elif event.type == pygame.USEREVENT and event.button == audio_button:
        print("Кнопка 'Настройки аудио' была нажата!")
        fade()
        # переход на страницу "НАСТРОЙКИ АУДИО"
        page = 2
        return page

    elif event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        # переход на страницу "ГЛАВНОЕ МЕНЮ"
        page = 0
        return page
    else:
        return 1