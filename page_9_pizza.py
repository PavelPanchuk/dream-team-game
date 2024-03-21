from button import ImageButton
import pygame
from fade import fade
import os
import datetime

MAX_FPS = 10

def resize_img(filename, width, height):
    img = pygame.image.load(filename)
    img = pygame.transform.scale(img, (width, height))
    return img

def init_pizza(width, height):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = width, height
    spice_button = ImageButton(
        WIDTH - WIDTH / 5,
        HEIGHT / 8,
        150,
        74,
        "приготовить",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png", "src/music/click.mp3")

    back_button = ImageButton(
        WIDTH / 2 - (252 / 2),
        HEIGHT / 2 + 52,
        252,
        74,
        "к заказу",
        "src/art/buttons/button1.png",
        "src/art/buttons/button2.png",
        "src/music/click.mp3",
    )
    return [back_button, spice_button]



def pizza_img(WIDTH,HEIGHT):
    global cheese_image, tomato_image, ham_image, mushroom_image, onion_image, pineapple_image, sausage_image,dough_mid_image
    # создаем поверхность для рисования пиццы


    file_path = "./src/art/ingredients/"

    # загружаем изображения теста и сыра
    dough_big_image = resize_img(f"{file_path}testo.png", (WIDTH / 2) * 1.5, (HEIGHT / 2) * 1.5)

    dough_mid_image = resize_img(f"{file_path}testo.png", (WIDTH / 2), (HEIGHT / 2))

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


    # создаем функцию для рисования
def draw_ingredients(pizza_surface,ingredient = None):
    # получаем координаты курсора мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # накладываем изображение ингредиента на поверхность пиццы с учетом смещения
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



def pizza(screen,WIDTH,HEIGHT):
    file_path = "./src/art/ingredients/"

    name_img = ["cheese", "ham", "mushroom", "onion", "pineapple", "sausage", "tomato", "testo"]
    x = WIDTH / 13
    y = HEIGHT / 4
    for i in name_img:

        # if (platform.system() == 'Linux'):
        image = pygame.image.load(f"{file_path}{i}.png")
        file_txt_path = f"{file_path}{i}.txt"
        # else:
        # прописать пути для винды
        # image = pygame.image.load("\\dreamteam\\src\\art\\guest\\" + random_image)
        # file_path = "\\dreamteam\\src\\txt\\" + random_text

        image = pygame.transform.scale(image, (WIDTH / 9, WIDTH / 9))
        screen.blit(image, (x, y))
        y += WIDTH / 8
        if i == "onion":
            x = WIDTH - WIDTH / 5
            y = HEIGHT / 4


def pizza_handler(event, buttons):
    back_button, spice_button = buttons

    # Возврат в меню

    if event.type == pygame.USEREVENT and event.button == back_button:
        fade()
        # переход на страницу "MENUS"
        page = 7
        return page

    elif event.type == pygame.USEREVENT and event.button == spice_button:
        # save_pizza()
        fade()
        # переход на страницу "GAME"
        page = 6
        return page
    else:
        return 9

def pizza_draw(pizza_surface,event):
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
        draw_ingredients(pizza_surface,"pineapple")

    if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
        draw_ingredients(pizza_surface,"sausage")

    if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
        draw_ingredients(pizza_surface,"tomat")

    if (event.type == pygame.KEYDOWN and event.key == pygame.K_5):
        draw_ingredients(pizza_surface,"cheese")

    if (event.type == pygame.KEYDOWN and event.key == pygame.K_6):
        draw_ingredients(pizza_surface,"ham")

    if (event.type == pygame.KEYDOWN and event.key == pygame.K_7):
        draw_ingredients(pizza_surface,"mushroom")

    if (event.type == pygame.KEYDOWN and event.key == pygame.K_8):
        draw_ingredients(pizza_surface,"onion")

    if (event.type == pygame.KEYDOWN and event.key == pygame.K_9):
        draw_ingredients(pizza_surface,"dough")

    # если пользователь нажал клавишу "S"
    #if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
        # вызываем функцию для сохранения изображения пиццы
        #save_pizza()

