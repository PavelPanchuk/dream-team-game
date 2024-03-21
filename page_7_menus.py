from button import ImageButton
import pygame
from fade import fade
import platform
import json
import os
from pygame import mixer
import shutil

def init_menus(WIDTH, HEIGHT):
    spice_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 148,
        252,
        74,
        "Рецепты",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    pizza_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 48,
        252,
        74,
        "к готовке пиццы",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    back_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 + 52,
        252,
        74,
        "к заказу",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    return [back_button, spice_button, pizza_button]

def menus_handler(event, buttons):
    back_button, spice_button, pizza_button = buttons

    # Возврат в меню

    if event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        # переход на страницу "GAME"
        page = 6
        return page

    elif event.type == pygame.USEREVENT and event.button == spice_button:
        fade()
        # переход на страницу "РЕЦЕПТЫ"
        page = 8
        return page
        #spice_window()

    elif event.type == pygame.USEREVENT and event.button == pizza_button:
        fade()
        # переход на страницу "ГОТОВКА"
        page = 9
        return page
        #pizza_window()

    else:
        return 7