import pygame
import sys
from button import ImageButton
import pygame_menu
import json
import os
import datetime
import platform


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

def resize_img(filename, width, height):
    img = pygame.image.load(filename)
    img = pygame.transform.scale(img, (width, height))
    return img

MAX_FPS = 10


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = resize_img("doska.jpg", WIDTH, HEIGHT)

clock = pygame.time.Clock()
WHITE = (0, 0, 255)

# Загрузка и установка курсора можно поменять на свою картинку, но хз на какую
#cursor = pygame.image.load("cursor.png")

sc = pygame.display.set_mode((400, 300))
sc.fill(WHITE)

pygame.display.update()
pygame.mouse.set_visible(False)  # Скрываем стандартный курсор

if (platform.system() == 'Linux'):
    file_path = "./src/art/ingredients/"
else:
    file_path = "\\src\\art\\ingredients\\"

# затемнение
def fade():
    WIDTH, HEIGHT = read_size()
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
        clock.tick(30)  # Ограничение FPS

#функция где можно готовить пиццу

def pizza_window():
    WIDTH, HEIGHT = read_size()
    running = False
    print("pizza cookie def")
    # Создание кнопок
    spice_button = ImageButton(WIDTH - WIDTH / 5, HEIGHT / 8, 150, 74, "приготовить", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    back_button = ImageButton(WIDTH / 13, HEIGHT / 8, 150, 74, "к заказу", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")

    # создаем поверхность для рисования пиццы
    pizza_surface = pygame.Surface(( HEIGHT/2, HEIGHT/2))
    pizza_surface.fill((0, 0, 0)) # белый цвет
    pizza_surface.set_alpha(200) # полупрозрачность
    pizza_rect = pizza_surface.get_rect()
    pizza_rect.center = (WIDTH/2, HEIGHT/2) # центр экрана


    file_path = "./src/art/ingredients/"


    # загружаем изображения теста и сыра
    dough_big_image = resize_img(f"{file_path}testo.png", (WIDTH/2) * 1.5, (HEIGHT/2) * 1.5)
    dough_mid_image = resize_img(f"{file_path}testo.png", (WIDTH/2), (HEIGHT/2))
    dough_small_image = resize_img(f"{file_path}testo.png", (WIDTH / 2) * 0.5, (HEIGHT / 2) * 0.5)



    # прописать пути для винды
    # image = pygame.image.load("\\dreamteam\\src\\art\\guest\\" + random_image)
    # file_path = "\\dreamteam\\src\\txt\\" + random_text


    cheese_image = resize_img(f"{file_path}cheese.png", 100, 100)
    tomato_image = resize_img(f"{file_path}tomato.png", 100, 100)
    ham_image = resize_img(f"{file_path}ham.png", 100, 100)
    mushroom_image = resize_img(f"{file_path}mushroom.png", 100, 100)
    onion_image = resize_img(f"{file_path}onion.png", 100, 100)
    pineapple_image = resize_img(f"{file_path}pineapple.png", 100, 100)
    sausage_image = resize_img(f"{file_path}sausage.png", 100, 100)


    def ingredients(name):
        if (name ==  "cheese"):
            return cheese_image
        elif (name ==  "tomat"):
            return tomato_image
        elif (name == "ham"):
            return ham_image
        elif (name == "mushroom"):
            return mushroom_image
        elif (name == "onion"):
            return onion_image
        elif (name == "pineapple"):
            return pineapple_image
        elif (name == "sausage"):
            return sausage_image
        elif (name == "dough"):

            return dough_mid_image


    # создаем функцию для рисования теста
    def draw_ingredients(ingredient = None):
        # получаем координаты курсора мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # вычисляем смещение относительно центра поверхности пиццы
        # накладываем изображение сыра на поверхность пиццы с учетом смещения
        image = ingredients(ingredient)
        pizza_surface.blit(image, (mouse_x-WIDTH/4 - image.get_rect().size[0] / 2, mouse_y-HEIGHT/4 - image.get_rect().size[1] / 2))

        # определяем файл
        file_path = f"{ingredient}.txt"
        file = open(file_path, "r")
        # считываем из файла
        num = int(file.read())
        file.close()
        result = int(num) + 1
        print(f"Вы потратили {result} ед. {ingredient}")
        # определяем файл
        file_path = f"{ingredient}.txt"
        os.remove(file_path)
        # запись в файл
        file = open(file_path, "w+")
        # пишем в файл
        file.write(str(result))
        file.close()
        # обновляем экран
        pygame.display.flip()
        clock.tick(MAX_FPS)


    # создаем функцию для сохранения изображения пиццы
    def save_pizza():
        # получаем текущую дату и время
        now = datetime.datetime.now()
        # форматируем дату и время в виде строки
        date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
        # задаем имя файла с датой и временем
        file_name = f"\\dreamteam\\src\\mission\\pizza\\pizza_{date_str}.png"
        # сохраняем изображение пиццы в файл
        pygame.image.save(pizza_surface, file_name)
        # выводим сообщение об успешном сохранении
        print(f"Изображение пиццы сохранено в файл {file_name}")

    running = True
    while running:
        screen.fill((0, 0, 0))
        background = resize_img("doska.jpg", WIDTH, HEIGHT)
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Кухня", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT / 7))
        screen.blit(text_surface, text_rect)

        name_img = ["cheese", "ham", "mushroom", "onion", "pineapple", "sausage", "tomato", "testo"]
        x = WIDTH / 13
        y = HEIGHT / 4
        for i in name_img:

            #if (platform.system() == 'Linux'):
            image = pygame.image.load(f"{file_path}{i}.png")
            file_txt_path = f"{file_path}{i}.txt"
            #else:
                #прописать пути для винды
                #image = pygame.image.load("\\dreamteam\\src\\art\\guest\\" + random_image)
                #file_path = "\\dreamteam\\src\\txt\\" + random_text

            image = pygame.transform.scale(image, (WIDTH / 9 , WIDTH / 9 ))
            screen.blit(image, (x, y))
            y += WIDTH / 8
            if i == "onion":
                x = WIDTH - WIDTH / 5
                y = HEIGHT / 4

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
            if event.type == pygame.USEREVENT and event.button == spice_button:
                save_pizza()


            for btn in [spice_button, back_button]:
                btn.handle_event(event)


            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # получаем координаты курсора мыши
                #mouse_x, mouse_y = pygame.mouse.get_pos()
                # если курсор находится над кнопкой "тесто"

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                draw_ingredients("pineapple")
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                draw_ingredients("sausage")
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                draw_ingredients("tomat")
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_5):
                draw_ingredients("cheese")
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_6):
                draw_ingredients("ham")
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_7):
                draw_ingredients("mushroom")
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_8):
                draw_ingredients("onion")
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_9):
                draw_ingredients("dough")
            # если пользователь нажал клавишу "S"
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                # вызываем функцию для сохранения изображения пиццы
                save_pizza()

        # рисуем поверхность пиццы на экране
        screen.blit(pizza_surface, pizza_rect)
        # обновляем экран

        for btn in [spice_button, back_button]:
        #for btn in [spice_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        #x, y = pygame.mouse.get_pos()
        #screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()
        clock.tick(MAX_FPS)


