import pygame
import sys
from button import ImageButton
import pygame_menu
import json


# Инициализация pygame
pygame.init()

file = open("settings.json", "r")

# читаем содержимое файла и преобразуем его в словарь
data = json.loads(file.read())

# получаем значение по ключу 'WIDTH' и присваиваем его переменной x
WIDTH = data["WIDTH"]
HEIGHT = data["HEIGHT"]
MAX_FPS = data["HEIGHT"]
# закрываем файл
file.close()
# выводим значение переменной x


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("spice")
main_background = pygame.image.load("background1.jpg")
game_background = pygame.image.load("background2.jpg")

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


# функция где подсказка о рецептах


def spice_window():
    print("spice window")
    # Создание кнопок
    # spice_button = ImageButton(WIDTH/2-(252/2), 150, 252, 74, "Рецепты", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    # pizza_button = ImageButton(WIDTH/2-(252/2), 250, 252, 74, "пицца", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    back_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        350,
        252,
        74,
        "назад",
        "green_button2.jpg",
        "green_button2_hover.jpg",
        "click.mp3",
    )

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 25)
        text_surface = font.render(
            "Чтобы сварить кофе нужно сварить кофе. для пиццы нужно тесто.",
            True,
            (0, 0, 0),
        )
        text_surface1 = font.render("потом для пеперони сыр и томаты.", True, (0, 0, 0))
        text_surface2 = font.render("для мясной мясо и томаты", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)
        text_rect = text_surface1.get_rect(center=(WIDTH / 2, 200))
        screen.blit(text_surface1, text_rect)
        text_rect = text_surface2.get_rect(center=(WIDTH / 2, 300))
        screen.blit(text_surface2, text_rect)
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

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            """ if event.type == pygame.USEREVENT and event.button == spice_button:
                fade()
                spice_window()

            if event.type == pygame.USEREVENT and event.button == pizza_button:
                fade()
                pizza_window()
            """
            for btn in [back_button]:
                btn.handle_event(event)

        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()
