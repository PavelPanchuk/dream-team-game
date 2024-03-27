from button import ImageButton
import pygame
from fade import fade
import platform
import json
import os
from pygame import mixer
import shutil

def init_store(WIDTH, HEIGHT, file_path_buttons,file_path_ingredients, file_path_music):
    back_button = ImageButton(
        # WIDTH - 1000,
       100,
        # HEIGHT - 600,
        100,
        150,
        74,
        "назад",
        f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
    )

    dough_button = ImageButton(
        3 * WIDTH / 8 - 75,
        HEIGHT / 3 - 75,
        150,
        150,
        "",
        f"{file_path_ingredients}testo.png",
        f"{file_path_ingredients}testo.png",
        f"{file_path_music}click.mp3",
    )
    tomato_button = ImageButton(
        4 * WIDTH / 8 - 75,
        HEIGHT / 3 - 75,
        150,
        150,
        "",
        f"{file_path_ingredients}tomato.png",
        f"{file_path_ingredients}tomato.png",
        f"{file_path_music}click.mp3",
    )
    cheese_button = ImageButton(
        5 * WIDTH / 8 - 75,
        HEIGHT / 3 - 75,
        150,
        150,
        "",
        f"{file_path_ingredients}cheese.png",
        f"{file_path_ingredients}cheese.png",
        f"{file_path_music}click.mp3",
    )
    sausage_button = ImageButton(
        6 * WIDTH / 8 - 75,
        HEIGHT / 3 - 75,
        150,
        150,
        "",
        f"{file_path_ingredients}sausage.png",
        f"{file_path_ingredients}sausage.png",
        f"{file_path_music}click.mp3",
    )
    mushroom_button = ImageButton(
        3 * WIDTH / 8 - 75,
        2 * HEIGHT / 3 - 75,
        150,
        150,
        "",
        f"{file_path_ingredients}mushroom.png",
        f"{file_path_ingredients}mushroom.png",
        f"{file_path_music}click.mp3",
    )
    onion_button = ImageButton(
        # WIDTH - 1000,
        4 * WIDTH / 8 - 75,
        2 * HEIGHT / 3 - 75,
        150,
        150,
        "",
        f"{file_path_ingredients}onion.png",
        f"{file_path_ingredients}onion.png",
        f"{file_path_music}click.mp3",
    )
    ham_button = ImageButton(
        # WIDTH - 1000,
        5 * WIDTH / 8 - 75,
        2 * HEIGHT / 3 - 75,
        150,
        150,
        "",
        f"{file_path_ingredients}ham.png",
        f"{file_path_ingredients}ham.png",
        f"{file_path_music}click.mp3",
    )
    pineapple_button = ImageButton(
        # WIDTH - 1000,
        6 * WIDTH / 8 - 75,
        2 * HEIGHT / 3 - 75,
        150,
        150,
        "",
        f"{file_path_ingredients}pineapple.png",
        f"{file_path_ingredients}pineapple.png",
        f"{file_path_music}click.mp3",
    )

    return [back_button, dough_button, tomato_button, cheese_button, sausage_button, mushroom_button, onion_button, ham_button, pineapple_button]



def store_handler(event, buttons):
    back_button, dough_button, tomato_button, cheese_button, sausage_button, mushroom_button, onion_button, ham_button, pineapple_button = buttons

    # Возврат в меню

    if event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        # переход на страницу "MENUS"
        page = 7
        return page

    else:
        return 10