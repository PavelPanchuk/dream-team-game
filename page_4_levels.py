from button import ImageButton
import pygame
from fade import fade
import sys
import main

def init_levels(WIDTH, HEIGHT, file_path_buttons, file_path_music):
    back_button = ImageButton(
        # WIDTH - 1000,
        WIDTH - 250,
        # HEIGHT - 600,
        100,
        150,
        74,
        "Назад",f"{file_path_buttons}button1.png",
        f"{file_path_buttons}button2.png",
        f"{file_path_music}click.mp3",
    )

    level_0_button = ImageButton(
        WIDTH / 2 - 400,
        HEIGHT / 2 - 105,
        180,
        180,
        "0",
        f"{file_path_buttons}level1.png",
        f"{file_path_buttons}level2.png",
        f"{file_path_music}click.mp3",
    )

    level_1_button = ImageButton(
        WIDTH / 2 - 200,
        HEIGHT / 2 - 105,
        180,
        180,
        "1",
        f"{file_path_buttons}level1.png",
        f"{file_path_buttons}level2.png",
        f"{file_path_music}click.mp3",
    )

    level_2_button = ImageButton(
        WIDTH / 2,
        HEIGHT / 2 - 105,
        180,
        180,
        "2",
        f"{file_path_buttons}level1.png",
        f"{file_path_buttons}level2.png",
        f"{file_path_music}click.mp3",
    )

    level_3_button = ImageButton(
        WIDTH / 2 + 200,
        HEIGHT / 2 - 105,
        180,
        180,
        "3",
        f"{file_path_buttons}level1.png",
        f"{file_path_buttons}level2.png",
        f"{file_path_music}click.mp3",
    )

    level_4_button = ImageButton(
        WIDTH / 2 - 400,
        HEIGHT / 2 + 90,
        180,
        180,
        "4",
        f"{file_path_buttons}level1.png",
        f"{file_path_buttons}level2.png",
        f"{file_path_music}click.mp3",
    )

    level_5_button = ImageButton(
        WIDTH / 2 - 200,
        HEIGHT / 2 + 90,
        180,
        180,
        "5",
        f"{file_path_buttons}level1.png",
        f"{file_path_buttons}level2.png",
        f"{file_path_music}click.mp3",
    )

    level_6_button = ImageButton(
        WIDTH / 2,
        HEIGHT / 2 + 90,
        180,
        180,
        "6",
        f"{file_path_buttons}level1.png",
        f"{file_path_buttons}level2.png",
        f"{file_path_music}click.mp3",
    )

    level_7_button = ImageButton(
        WIDTH / 2 + 200,
        HEIGHT / 2 + 90,
        180,
        180,
        "7",
        f"{file_path_buttons}level1.png",
        f"{file_path_buttons}level2.png",
        f"{file_path_music}click.mp3",
    )
    return [back_button, level_0_button, level_1_button,
            level_2_button, level_3_button, level_4_button,
            level_5_button, level_6_button, level_7_button]


def levels_handler(event, buttons):
    (back_button, level_0_button, level_1_button,
     level_2_button, level_3_button, level_4_button,
     level_5_button, level_6_button, level_7_button) = buttons

    if event.type == pygame.USEREVENT and event.button == level_0_button:
        fade()
        # переход на страницу "STORY_START"
        page = 5
        return page

    elif event.type == pygame.USEREVENT and event.button == level_1_button:
        fade()
        # переход на страницу "NEW_GAME"
        page = 6
        return page


    elif event.type == pygame.USEREVENT and event.button == level_2_button:
        fade()
        # переход на страницу "NEW_GAME"
        page = 6
        return page

    elif event.type == pygame.USEREVENT and event.button == level_3_button:
        fade()
        # переход на страницу "NEW_GAME"
        page = 6
        return page

    elif event.type == pygame.USEREVENT and event.button == level_4_button:
        fade()
        # переход на страницу "NEW_GAME"
        page = 6
        return page

    elif event.type == pygame.USEREVENT and event.button == level_5_button:
        fade()
        # переход на страницу "NEW_GAME"
        page = 6
        return page

    elif event.type == pygame.USEREVENT and event.button == level_6_button:
        fade()
        # переход на страницу "NEW_GAME"
        page = 6
        return page

    elif event.type == pygame.USEREVENT and event.button == level_7_button:
        fade()
        # переход на страницу "NEW_GAME"
        page = 6
        return page

    elif event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        # переход на страницу "ГЛАВНОЕ МЕНЮ"
        page = 0
        return page

    else:
        return 4