from button import ImageButton
import pygame
from fade import fade
import sys

def init_video(WIDTH,HEIGHT):
    low_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 - 105,
        400,
        74,
        "960x600",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3"
    )

    full_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 - 30,
        400,
        74, "1280x640",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3"
    )
    hd_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 45, 400,
        74, "1920x1080",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3"
    )

    back_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 120,
        400,
        74,
        "Назад",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3"
    )
    return [low_button,full_button,hd_button, back_button]


def video_handler(screen, event, buttons):
    low_button,full_button,hd_button, back_button = buttons
    if event.type == pygame.USEREVENT and event.button == hd_button:
        file = open('settings.json', 'w+')
        # записываем текст в файл
        file.write('{"WIDTH": 1920, "HEIGHT": 1080,"MAX_FPS":60}')
        # закрываем файл
        file.close()
        return 3

    elif event.type == pygame.USEREVENT and event.button == full_button:
        file = open('settings.json', 'w+')
        # записываем текст в файл
        file.write('{"WIDTH": 1280, "HEIGHT": 1024,"MAX_FPS":60}')
        # закрываем файл
        file.close()
        return 3

    elif event.type == pygame.USEREVENT and event.button == low_button:
        file = open('settings.json', 'w+')
        # записываем текст в файл
        file.write('{"WIDTH": 960, "HEIGHT": 600,"MAX_FPS":60}')
        # закрываем файл
        file.close()
        return 3

    elif event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        page = 1
        return page
    else:
        return 3


