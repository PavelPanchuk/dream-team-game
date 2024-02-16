import pygame
import sys
from button import ImageButton
import pygame_menu
import json


from pizza_window import pizza_window
from spice_window import spice_window
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
print(WIDTH) 
print(HEIGHT) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = pygame.image.load("background1.jpg")
game_background = pygame.image.load("background2.jpg")

clock = pygame.time.Clock()









# загружаем изображения спрайтов
dough = pygame.image.load("dough.png")
cheese = pygame.image.load("cheese.png")
tomato = pygame.image.load("tomat.png")

# создаем прямоугольники для спрайтов
dough_rect = dough.get_rect()
cheese_rect = cheese.get_rect()
tomato_rect = tomato.get_rect()

# задаем начальные позиции для спрайтов
dough_rect.center = (100, 300)
cheese_rect.center = (100, 200)
tomato_rect.center = (100, 400)

# создаем переменные для подсчета количества сыра и томатов
cheese_count = 0
tomato_count = 0

# создаем переменную для проверки, положил ли игрок тесто
dough_placed = False

# создаем переменную для проверки, правильно ли сделана пицца
pizza_done = False


















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

        
def menus():
    print("menu def")
    # Создание кнопок
    spice_button = ImageButton(WIDTH/2-(252/2), 150, 252, 74, "Рецепты", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    pizza_button = ImageButton(WIDTH/2-(252/2), 250, 252, 74, "к готовке пиццы", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")
    back_button = ImageButton(WIDTH/2-(252/2), 350, 252, 74, "к заказу", "green_button2.jpg", "green_button2_hover.jpg", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("управление кафе", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2,100))
        screen.blit(text_surface, text_rect)






























        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # получаем позицию курсора
                pos = event.pos
                # если курсор находится над спрайтом сыра
                if cheese_rect.collidepoint(pos):
                    # увеличиваем счетчик сыра на 1
                    global cheese_count
                    cheese_count=cheese_count +1
                # если курсор находится над спрайтом томата
                if tomato_rect.collidepoint(pos):
                    # увеличиваем счетчик томата на 1
                    global tomato_count
                    tomato_count=tomato_count +1
                # если курсор находится над спрайтом теста
                if dough_rect.collidepoint(pos):
                    # перемещаем тесто в центр экрана
                    dough_rect.center = (400, 300)
                    # устанавливаем флаг, что тесто положено
                    dough_placed = True

            # проверяем, правильно ли сделана пицца
            # для этого нужно, чтобы игрок положил тесто и нажал на сыр 10 раз и на томат 5 раз













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
                fade()
                spice_window()

            if event.type == pygame.USEREVENT and event.button == pizza_button:
                fade()
                pizza_window()
                

            for btn in [spice_button, pizza_button, back_button]:
                btn.handle_event(event)

        for btn in [spice_button, pizza_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)





        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-2, y-2))










        screen.fill((255, 255, 255))

        # рисуем спрайты на экране
        screen.blit(dough, dough_rect)
        screen.blit(cheese, cheese_rect)
        screen.blit(tomato, tomato_rect)
    global pizza_done
        # если пицца готова, выводим сообщение об успехе
    if (pizza_done==True):
            # создаем шрифт
        font = pygame.font.SysFont("Arial", 32)
            # создаем текст
        text = font.render("Пицца готова!", True, (0, 0, 0))
            # создаем прямоугольник для текста
        text_rect = text.get_rect()
            # задаем позицию для текста
        text_rect.center = (400, 500)
            # рисуем текст на экране
        screen.blit(text, text_rect)







        if (dough_placed==False) and cheese_count == 10 and tomato_count == 5:
                        # устанавливаем флаг, что пицца готова
            pizza_done = True







        pygame.display.flip()


