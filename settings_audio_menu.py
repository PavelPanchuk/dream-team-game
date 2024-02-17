
import pygame
import sys
from button import ImageButton
import pygame_menu
import json


# Инициализация pygame
pygame.init()

def read_size():
    file = open("settings.json", "r")
    data = json.loads(file.read())

    # Параметры экрана

    width = data["WIDTH"]
    height = data["HEIGHT"]
    file.close()
    return width, height

WIDTH, HEIGHT = read_size()

MAX_FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = pygame.image.load("background1.jpg")
main_background = pygame.transform.scale(main_background, (WIDTH, HEIGHT))

game_background = pygame.image.load("background2.jpg")
game_background = pygame.transform.scale(game_background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Загрузка и установка курсора можно поменять на свою картинку, но хз на какую
cursor = pygame.image.load("cursor.png") 
pygame.mouse.set_visible(True)  # Скрываем стандартный курсор
# затемнение
def fade():
    running = True
    fade_alpha = 0  # Уровень прозрачности для анимации

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
        clock.tick(MAX_FPS)  # Ограничение FPS

def settings_audio_menu():
    print("audio settings")

    # Проверка работает ли музыка
    if pygame.mixer.music.get_busy():
        text_music = "Отключить музыку"
    else:
        text_music = "Включить музыку"

        # Создание кнопок
    on_button = ImageButton(WIDTH/2-(252/2), HEIGHT / 2 - 74, 252, 74, text_music, "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    back_button = ImageButton(WIDTH/2-(252/2), HEIGHT / 2 + 26 , 252, 74, "Назад", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Изменить настройки звука", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2,100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False


            if event.type == pygame.USEREVENT and event.button == on_button:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    on_button.updateText("Включить музыку", screen)

                else:
                    pygame.mixer.music.unpause()
                    on_button.updateText("Отключить музыку", screen)


            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [on_button, back_button]:
                btn.handle_event(event)

        for btn in [on_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()
#меню готовка кухня короче

