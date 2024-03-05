import pygame
import json
from pygame import mixer


def read_size():
    file = open("settings.json", "r")
    data = json.loads(file.read())

    # Параметры экрана

    width = data["WIDTH"]
    height = data["HEIGHT"]
    file.close()
    return width, height

WIDTH, HEIGHT = read_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def fade():
    running = True
    fade_alpha = 0  # Уровень прозрачности для анимации
    WIDTH, HEIGHT = read_size()
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Анимация затухания текущего экрана
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        # Увеличение уровня прозрачности
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(30)  # Ограничение FPS