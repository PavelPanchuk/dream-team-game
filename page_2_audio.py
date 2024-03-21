from button import ImageButton
import pygame
from fade import fade
import sys

def init_audio(WIDTH,HEIGHT):
    if pygame.mixer.music.get_busy():
        text_music = "Отключить музыку"
    else:
        text_music = "Включить музыку"

    on_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 - 80, 400, 74,
        text_music,
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3"
    )
    back_button = ImageButton(
        WIDTH / 2 - (400 / 2) - 230,
        HEIGHT / 2 + 20,
        400,
        74,
        "Назад",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png", "src/music/click.mp3"
    )
    return [on_button, back_button]


def audio_handler(screen, event, buttons):
    on_button, back_button = buttons
    if event.type == pygame.USEREVENT and event.button == on_button:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            on_button.updateText("Включить музыку", screen)

        else:
            pygame.mixer.music.unpause()
            on_button.updateText("Отключить музыку", screen)

        return 2

    elif event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        page = 1
        return page
    else:
        return 2
