from button import ImageButton
import pygame
from fade import fade
import platform
import json
import os
from pygame import mixer
import shutil

def init_recipes(WIDTH, HEIGHT):
    back_button = ImageButton(
        # WIDTH - 1000,
        100,
        # HEIGHT - 600,
        100,
        150,
        74,
        "назад",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    return [back_button]


def recipes_img(WIDTH):
    global imge_recipes_hawaiian,imge_recipes_pepperoni,imge_recipes_newyork,imge_recipes_margherita
    file_path = "./src/art/recipes/"
    imge_recipes_hawaiian = pygame.image.load(f"{file_path}recipes_hawaiian.jpg")
    imge_recipes_hawaiian = pygame.transform.scale(imge_recipes_hawaiian, (WIDTH / 4, WIDTH / 8))
    imge_recipes_pepperoni = pygame.image.load(f"{file_path}recipes_pepperoni.jpg")
    imge_recipes_pepperoni = pygame.transform.scale(imge_recipes_pepperoni, (WIDTH / 4, WIDTH / 8))
    imge_recipes_newyork = pygame.image.load(f"{file_path}recipes_newyork.jpg")
    imge_recipes_newyork = pygame.transform.scale(imge_recipes_newyork, (WIDTH / 4, WIDTH / 8))
    imge_recipes_margherita = pygame.image.load(f"{file_path}recipes_margherita.jpg")
    imge_recipes_margherita = pygame.transform.scale(imge_recipes_margherita, (WIDTH / 4, WIDTH / 8))


def recipes(screen,WIDTH,HEIGHT):
    screen.blit(imge_recipes_hawaiian, (WIDTH / 2 - 1.5 * WIDTH / 4, 0.5 * HEIGHT / 2))
    screen.blit(imge_recipes_pepperoni, (WIDTH / 2, 0.5 * HEIGHT / 2))
    screen.blit(imge_recipes_newyork, (WIDTH / 2 - 1.5 * WIDTH / 4, HEIGHT / 2))
    screen.blit(imge_recipes_margherita, (WIDTH / 2, HEIGHT / 2))

def recipes_handler(event, buttons):
    back_button = buttons[0]

    # Возврат в меню

    if event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        # переход на страницу "MENUS"
        page = 7
        return page

    else:
        return 8