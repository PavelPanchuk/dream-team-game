from button import ImageButton
import pygame
from fade import fade
import platform
import json
import os
from pygame import mixer
import shutil

"магазин",


def init_menus(WIDTH, HEIGHT, file_path_buttons, file_path_music):
    spice_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 - 105,
        252,
        74,
        "Рецепты",
        f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
    )
    pizza_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 - 30,
        252,
        74,
        "к готовке пиццы",
        f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
    )
    store_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 45,
        252,
        74,
        "магазин",
        f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
    )

    back_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 120,
        252,
        74,
        "к заказу",
        f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
    )

    return [back_button, store_button, spice_button, pizza_button]

def menus_handler(event, buttons):
    back_button, store_button, spice_button, pizza_button = buttons

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

    elif event.type == pygame.USEREVENT and event.button == store_button:
        fade()
        # переход на страницу "Магазин"
        page = 10
        return page

    else:
        return 7