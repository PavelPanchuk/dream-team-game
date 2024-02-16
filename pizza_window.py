import pygame
import sys
from button import ImageButton
import pygame_menu
import json

import datetime


# Инициализация pygame
pygame.init()

file = open('settings.json', 'r')

    # читаем содержимое файла и преобразуем его в словарь
data = json.loads(file.read())

    # получаем значение по ключу 'WIDTH' и присваиваем его переменной x
WIDTH = data['WIDTH']
HEIGHT= data['HEIGHT']
MAX_FPS= data['HEIGHT']
    # закрываем файл
file.close()
    # выводим значение переменной x


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = pygame.image.load("background1.jpg")
game_background = pygame.image.load("background2.jpg")

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
        clock.tick(MAX_FPS)  # Ограничение FPS

#функция где можно готовить пиццу

def pizza_window():
    print("pizza cookie def")
    # Создание кнопок
    spice_button = ImageButton(WIDTH/2-200, 350, 100, 74, "приготовить", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    pizza_button = ImageButton(WIDTH/2-200, 450, 100, 74, "сыр", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    back_button = ImageButton(WIDTH/2-200, 550, 100, 74, "к заказу", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")



    # создаем кнопку "тесто"
    dough_button = pygame.sprite.Sprite()
    dough_button.image = pygame.image.load("dough.png")
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
    pizza_surface = pygame.Surface((500, 300))
    pizza_surface.fill((0, 0, 0)) # белый цвет
    pizza_surface.set_alpha(128) # полупрозрачность
    pizza_rect = pizza_surface.get_rect()
    pizza_rect.center = (500, 300) # центр экрана

    # загружаем изображения теста и сыра
    dough_image = pygame.image.load("dough.png")
    dough_image = pygame.transform.scale(dough_image, (300, 300)) # подгоняем под размер поверхности

    cheese_image = pygame.image.load("cheese.png")
    cheese_image = pygame.transform.scale(cheese_image, (50, 50)) # подгоняем под размер кусочка сыра


    tomat_image = pygame.image.load("tomat.png")
    tomat_image = pygame.transform.scale(tomat_image, (50, 50)) # подгоняем под размер кусочка сыра


    # создаем функцию для рисования теста
    def draw_dough():
        # накладываем изображение теста на поверхность пиццы
        pizza_surface.blit(dough_image, (mouse_x-300, mouse_y-150))
        # обновляем экран

        pygame.display.flip()

    # создаем функцию для рисования сыра
    def draw_cheese():
        # получаем координаты курсора мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # вычисляем смещение относительно центра поверхности пиццы
        # накладываем изображение сыра на поверхность пиццы с учетом смещения
        pizza_surface.blit(cheese_image, (mouse_x-300, mouse_y-150))
        # обновляем экран
        pygame.display.flip()

    def draw_tomat():
        # получаем координаты курсора мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # вычисляем смещение относительно центра поверхности пиццы
        # накладываем изображение сыра на поверхность пиццы с учетом смещения
        pizza_surface.blit(tomat_image, (mouse_x-300, mouse_y-150))
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














    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("кухня", True, (0, 0, 0))
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

            if event.type == pygame.USEREVENT and event.button == pizza_button:
                pass

            for btn in [spice_button, pizza_button, back_button]:
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



        for btn in [spice_button, pizza_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        







        # Отображение курсора в текущей позиции мыши
        #x, y = pygame.mouse.get_pos()
        #screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()


