import pygame
import sys
from button import ImageButton
import pygame_menu
import json
import os
import datetime


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

def resize_background(filename, width, height):
    background = pygame.image.load(filename)
    background = pygame.transform.scale(background, (width, height))
    return background

MAX_FPS = 10


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = resize_background("doska.jpg", WIDTH, HEIGHT)

clock = pygame.time.Clock()
WHITE = (0, 0, 255)

# Загрузка и установка курсора можно поменять на свою картинку, но хз на какую
#cursor = pygame.image.load("cursor.png")

sc = pygame.display.set_mode((400, 300))
sc.fill(WHITE)

pygame.display.update()
pygame.mouse.set_visible(False)  # Скрываем стандартный курсор
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
        clock.tick(30)  # Ограничение FPS

#функция где можно готовить пиццу

def pizza_window():
    WIDTH, HEIGHT = read_size()
    running = False
    print("pizza cookie def")
    # Создание кнопок
    spice_button = ImageButton(WIDTH-200, 100, 150, 74, "приготовить", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    back_button = ImageButton(100, 100, 150, 74, "к заказу", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    """
    chese_button = ImageButton(WIDTH-200, 200, 100, 100, "", "src/art/ingredients/cheese.png", "src/art/ingredients/cheese.png", "click.mp3")
    ham_button = ImageButton(WIDTH-200, 300, 100, 100, "", "src/art/ingredients/ham.png", "src/art/ingredients/ham.png", "click.mp3")
    mushroom_button = ImageButton(WIDTH-200, 400, 100, 100, "", "src/art/ingredients/mushroom.png", "src/art/ingredients/mushroom.png", "click.mp3")
    onion_button = ImageButton(WIDTH-200, 500, 100, 100, "", "src/art/ingredients/onion.png", "src/art/ingredients/onion.png", "click.mp3")

    pineapple_button = ImageButton(100, 200, 100, 100, "", "src/art/ingredients/pineapple.png", "src/art/ingredients/pineapple.png", "click.mp3")
    sausage_button = ImageButton(100, 300, 100, 100, "", "src/art/ingredients/sausage.png", "src/art/ingredients/sausage.png", "click.mp3")
    tomato_button = ImageButton(100, 400, 100, 100, "", "src/art/ingredients/tomato.png", "src/art/ingredients/tomato.png", "click.mp3")
    testo_button = ImageButton(100, 500, 100, 100, "", "src/art/ingredients/testo.png", "src/art/ingredients/testo.png", "click.mp3")
    """



    # создаем кнопку "тесто"
    dough_button = pygame.sprite.Sprite()
    dough_button.image = pygame.image.load("testo.png")
    dough_button.rect = dough_button.image.get_rect()
    dough_button.rect.x =10000
    dough_button.rect.y = 10000

    # создаем кнопку "сыр"
    cheese_button = pygame.sprite.Sprite()
    cheese_button.image = pygame.image.load("cheese.png")
    cheese_button.rect = cheese_button.image.get_rect()
    cheese_button.rect.x = 10000
    cheese_button.rect.y = 10000


    # создаем кнопку "tomat"
    tomat_button = pygame.sprite.Sprite()
    tomat_button.image = pygame.image.load("tomat.png")
    tomat_button.rect = tomat_button.image.get_rect()
    tomat_button.rect.x = 10000
    tomat_button.rect.y = 10000

    # создаем группу для кнопок
    buttons = pygame.sprite.Group()
    buttons.add(dough_button)
    buttons.add(cheese_button)
    buttons.add(tomat_button)


    # создаем поверхность для рисования пиццы
    pizza_surface = pygame.Surface((WIDTH/2, HEIGHT/2))
    pizza_surface.fill((0, 0, 0)) # белый цвет
    pizza_surface.set_alpha(128) # полупрозрачность
    pizza_rect = pizza_surface.get_rect()
    pizza_rect.center = (WIDTH/2, HEIGHT/2) # центр экрана

    # загружаем изображения теста и сыра
    dough_image = pygame.image.load("testo.png")
    dough_image = pygame.transform.scale(dough_image, (WIDTH/2, HEIGHT/2)) # подгоняем под размер поверхности

    cheese_image = pygame.image.load("cheese.png")
    cheese_image = pygame.transform.scale(cheese_image, (50, 50)) # подгоняем под размер кусочка сыра


    tomat_image = pygame.image.load("tomat.png")
    tomat_image = pygame.transform.scale(tomat_image, (50, 50)) # подгоняем под размер кусочка сыра


    # создаем функцию для рисования теста
    def draw_dough():
        # накладываем изображение теста на поверхность пиццы
        pizza_surface.blit(dough_image, (mouse_x-WIDTH/2, mouse_y-HEIGHT/2))
        # обновляем экран

        file_path = "dough.txt"
        file = open(file_path, "r")
        num = int(file.read())
        file.close()
        x=1
        result = int(num) + int(x)
        print(result)
        print(num)

        file_path = "dough.txt"
        os.remove(file_path)

        file = open(file_path, "w+")
        file.write(str(result))
        file.close()

        pygame.display.flip()
        clock.tick(MAX_FPS)

    # создаем функцию для рисования сыра
    def draw_cheese():
        # получаем координаты курсора мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # вычисляем смещение относительно центра поверхности пиццы
        # накладываем изображение сыра на поверхность пиццы с учетом смещения
        pizza_surface.blit(cheese_image, (mouse_x-WIDTH/4, mouse_y-HEIGHT/4))
        # обновляем экран

        file_path = "cheese.txt"
        file = open(file_path, "r")
        num = int(file.read())
        file.close()
        x=1
        result = int(num) + int(x)
        print(result)
        print(num)

        file_path = "cheese.txt"
        os.remove(file_path)

        file = open(file_path, "w+")
        file.write(str(result))
        file.close()
        pygame.display.flip()
        clock.tick(MAX_FPS)

    def draw_tomat():
        # получаем координаты курсора мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # вычисляем смещение относительно центра поверхности пиццы
        # накладываем изображение сыра на поверхность пиццы с учетом смещения
        pizza_surface.blit(tomat_image, (mouse_x-WIDTH/4, mouse_y-HEIGHT/4))
        # обновляем экран
        

        file_path = "tomat.txt"
        file = open(file_path, "r")
        num = int(file.read())
        file.close()
        x=1
        result = int(num) + int(x)
        print(result)
        print(num)

        file_path = "tomat.txt"
        os.remove(file_path)

        file = open(file_path, "w+")
        file.write(str(result))
        file.close()

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
        background = resize_background("doska.jpg", WIDTH, HEIGHT)
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Кухня", True, (255, 255, 255))
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

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            if event.type == pygame.USEREVENT and event.button == spice_button:
                save_pizza()


            #for btn in [spice_button, back_button, chese_button, ham_button, mushroom_button, onion_button,pineapple_button, sausage_button, tomato_button, testo_button]:
            for btn in [spice_button, back_button]:
                btn.handle_event(event)




            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # получаем координаты курсора мыши
                #mouse_x, mouse_y = pygame.mouse.get_pos()
                # если курсор находится над кнопкой "тесто"
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button ==2 ):
                    # вызываем функцию для рисования теста
                mouse_x, mouse_y = pygame.mouse.get_pos()

                print("тесто")
                draw_dough()
                # если курсор находится над кнопкой "сыр"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d or(event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 ):
                    # вызываем функцию для рисования сыра
                draw_cheese()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_a) or(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 ):
                    # вызываем функцию для рисования сыра
                draw_tomat()
            # если пользователь нажал клавишу "S"
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                # вызываем функцию для сохранения изображения пиццы
                save_pizza()
       
        # рисуем кнопки на экране
        buttons.draw(screen)
        # рисуем поверхность пиццы на экране
        screen.blit(pizza_surface, pizza_rect)
        # обновляем экран

        #for btn in [spice_button, back_button, chese_button, ham_button, mushroom_button, onion_button,
        #            pineapple_button, sausage_button, tomato_button, testo_button]:
        for btn in [spice_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        







        # Отображение курсора в текущей позиции мыши
        #x, y = pygame.mouse.get_pos()
        #screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()
        clock.tick(MAX_FPS)


