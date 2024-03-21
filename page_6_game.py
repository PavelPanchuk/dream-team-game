from button import ImageButton
import pygame
from fade import fade
import platform
import json
import os
from pygame import mixer
import shutil

def init_game(WIDTH, HEIGHT):
    back_button = ImageButton(
        0.2 * WIDTH,
        50,
        150,
        74,
        "Меню",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    menus_button = ImageButton(
        0.55 * WIDTH,
        3 * HEIGHT / 4 - 40,
        85 * (WIDTH // 300),
        74,
        "На кухню",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    put_button = ImageButton(
        0.55 * WIDTH,
        3 * HEIGHT / 4 + 50,
        85 * (WIDTH // 300),
        74,
        "Отдать заказ",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    return [back_button, menus_button, put_button]

def game(screen,WIDTH,HEIGHT):
    file_path = "src/txt/money.txt"
    file = open(file_path, "r")
    # читаем число из файла и преобразуем его в целое
    num = int(file.read())
    # закрываем файл
    file.close()
    # проверяем существование файла
    file_path = "src/txt/day.txt"

    # задаем другую переменную для сложения

    # открываем файл для чтения
    file = open(file_path, "r")

    # читаем число из файла и преобразуем его в целое
    day = int(file.read())

    file.close()

    # Загрузка изображений
    if (platform.system() == 'Linux'):
        image_guest = pygame.image.load("./src/art/guest/1/1_normal.png")
        image_bubble = pygame.image.load("./src/art/bubble.png")
        image_guest_txt = pygame.image.load("./src/art/guest/1/text_1.png")

        # file_path = "./src/txt/" + random_text
    else:
        image_guest = pygame.image.load("\\dreamteam\\src\\art\\guest\\1\\1_normal.png")
        image_bubble = pygame.image.load("\\dreamteam\\src\\art\\bubble.png")
        image_guest_txt = pygame.image.load("\\dreamteam\\src\\art\\guest\\1\\text_1.png")
    """ Вынести в функцию одинаковые части кода"""
    width, height = image_guest.get_size()
    # Уменьшение размера изображения
    image_guest = pygame.transform.scale(image_guest, (width // (6 / (HEIGHT // 300)), height // (6 / (HEIGHT // 300))))
    # получаем новые размеры изображения
    width, height = image_guest.get_size()
    # Размещение изображения на экране
    screen.blit(image_guest, (WIDTH / 3 - width / 2, 2 * HEIGHT / 3 - height))

    width, height = image_bubble.get_size()
    image_bubble = pygame.transform.scale(image_bubble,
                                          (width // (6 / (HEIGHT // 300)), height // (6 / (HEIGHT // 300))))
    width, height = image_bubble.get_size()
    screen.blit(image_bubble, (WIDTH / 2 - width / 2, HEIGHT / 3 - height))

    width, height = image_guest_txt.get_size()
    image_guest_txt = pygame.transform.scale(image_guest_txt,
                                             (width // (6 / (HEIGHT // 300)), height // (6 / (HEIGHT // 300))))
    width, height = image_guest_txt.get_size()
    screen.blit(image_guest_txt, (WIDTH / 2 - width / 2, HEIGHT / 3 - height))

def game_handler(event,screen, buttons,WIDTH,HEIGHT):
    back_button, menus_button, put_button = buttons

    # Возврат в меню

    if event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        # переход на страницу "LEVELS"
        page = 4
        return page

    # вызывается файл с функцией меню
    elif event.type == pygame.USEREVENT and event.button == menus_button:
        fade()
        # переход на страницу "MENUS"
        page = 7
        return page
        # storystart() level_choose()
    #  при нажатии на которую можно отдать заказ, сравнивает миссию и что получилось
    elif event.type == pygame.USEREVENT and event.button == put_button:
        # задаем путь к папке
        # получение инфы о миссии
        file = open("mission.json", "r")
        data = json.loads(file.read())
        random_cheese = data["random_cheese"]
        random_cheese = int(random_cheese)
        random_tomat = data["random_tomat"]
        random_tomat = int(random_tomat)
        random_dough = data["random_dough"]
        random_dough = int(random_dough)
        file.close()

        file_path = "src/txt/cheese.txt"
        file = open(file_path, "r")
        need_cheese = int(file.read())
        file.close()
        file_path = "src/txt/tomat.txt"
        file = open(file_path, "r")
        need_tomat = int(file.read())
        file.close()
        file_path = "src/txt/dough.txt"
        file = open(file_path, "r")
        need_dough = int(file.read())
        file.close()

        print("random_cheese" + str(random_cheese))
        print("need" + str(need_cheese))
        print("random_tomat" + str(random_tomat))
        print("need" + str(need_tomat))
        print("random_dough" + str(random_dough))
        print("need" + str(need_dough))

        if (random_cheese) <= (need_cheese) and (random_tomat) <= (need_tomat) and (random_dough) <= (need_dough):
            print(f"1 k 1 можно отдать заказ")

            file_path = "src/txt/money.txt"

            # задаем другую переменную для сложения
            other_var = int(random_cheese) * 200

            # открываем файл для чтения
            file = open(file_path, "r")

            # читаем число из файла и преобразуем его в целое
            num = int(file.read())

            # закрываем файл
            file.close()

            # нынешняя сумма + доходы-расходы фактические (тут можно отдать больше товаров чем просят, и это не оплачивается)
            result = int(num) + int(other_var) - 150
            print(result)
            print(num)
            print(other_var)

            # открываем файл для записи
            file = open(file_path, "w")

            # записываем результат в файл, преобразовав его в строку
            file.write(str(result))

            # закрываем файл
            file.close()

            # задаем путь к файлу
            file_path = "mission.json"
            # удаляем файл
            os.remove(file_path)

            # задаем путь к директории
            if (platform.system() == 'Linux'):
                dir_path = "./src/mission/pizza/"
            else:
                dir_path = "\\dreamteam\\src\\mission\\pizza\\"

            # удаляем директорию и все ее содержимое
            shutil.rmtree(dir_path)
            # задаем путь к директории
            if (platform.system() == 'Linux'):
                dir_path = "./src/mission/pizza"
            else:
                dir_path = "\\dreamteam\\src\\mission\\pizza"

            # создаем директорию
            os.mkdir(dir_path)

            file_path = "src/txt/tomat.txt"

            # удаляем файл
            os.remove(file_path)
            file_path = "src/txt/cheese.txt"

            # удаляем файл
            os.remove(file_path)

            file_path = "src/txt/dough.txt"
            # удаляем файл
            os.remove(file_path)


        else:
            font = pygame.font.Font(None, 72)
            text_surface = font.render(
                "ТУТ НЕ ВЕСЬ ЗАКАЗ", True, (0, 0, 0), (255, 204, 153)
            )
            text_rect = text_surface.get_rect(
                center=(WIDTH / 10 + 100, HEIGHT / 20 + 300)
            )
            screen.blit(text_surface, text_rect)
            mixer.init()

            # загружаем файл с музыкой
            mixer.music.load("src/music/error.mp3")

            # воспроизводим музыку бесконечно с начала
            mixer.music.play(0, 0.0)
            pygame.mixer.music.load("src/music/soundtreck.mp3")

            # воспроизводим музыку постоянно по кругу
            pygame.mixer.music.play(1)
        return 6
    else:
        return 6