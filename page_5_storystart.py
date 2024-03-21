from button import ImageButton
import pygame
from fade import fade
import platform

def init_storystart(WIDTH, HEIGHT):
    back_button = ImageButton(
        # WIDTH - 1000,
        WIDTH - 250,
        # HEIGHT - 600,
        100,
        150,
        74,
        "Назад",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )

    continue_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 - 148,
        252,
        74,
        "Окей, помогу!",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )

    return [back_button, continue_button]

def story(screen,WIDTH,HEIGHT):
    random_image = "ba.png"
    random_text = "storystart.txt"

    # Загрузка изображения  выбранной вайфу
    if (platform.system() == 'Linux'):
        image = pygame.image.load("./src/story/person/" + random_image)
        file_path = "./src/story/txt/" + random_text
    else:
        file_path = (random_text)
        image = pygame.image.load(random_image)
        # file_path =("\\dream-team-game-dev\\src\\story\\txt\\" + random_text)
        # image = pygame.image.load("\\dream-team-game-dev\\src\\story\\person\\" + random_image)

    # number= pygame.text.load()

    # открываем файл для чтения
    file = open(file_path, "r", encoding="utf-8")

    # читаем текст из файла и записываем его в переменную
    text = file.read()

    # закрываем файл
    file.close()
    # выводим текст на экран
    # print(text)

    '''
    text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
    screen.blit(text_surface, text_rect)
    '''
    # Координаты для размещения изображения

    x = 100
    y = 200
    width, height = image.get_size()

    # Уменьшение размера изображения в два раза
    image = pygame.transform.scale(image, (width // 5, height // 2))
    # Размещение изображения на экране
    screen.blit(image, (x, y))

    font = pygame.font.Font(None, 72)
    text_surface = font.render(str(text), True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
    screen.blit(text_surface, text_rect)

def story_handler(event, buttons):
    back_button, continue_button = buttons

    if event.type == pygame.USEREVENT and event.button == continue_button:
        fade()
        # переход на страницу ... РАЗВИТИЕ СЮЖЕТА
        #page =
        return 5

    elif event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        # переход на страницу "LEVELS"
        page = 4
        return page
    else:
        return 5