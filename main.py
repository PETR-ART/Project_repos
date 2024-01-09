import pygame
import random
import os


# для загрузки файлов
def load_image(name, colorkey=None):
    # Полный путь к файлу
    fullname = os.path.join('data/images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        pygame.quit()

    image = pygame.image.load(fullname)

    # для прозрачности изображения
    if colorkey is not None:
        image = image.convert()
        # если ключ -1, то убираем цвет который в левом нижнем углу
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    # отправляем изображение
    return image


America = {'США': 'Flag_USA.png', 'Канада': 'Flag_Canada.png', 'Мексика': 'Flag_Mexico.png', 'Куба': 'Flag_Cuba.png'}
Asia = {'Япония': 'Flag_Japan.png', 'Китай': 'Flag_China.png', 'Индия': 'Flag_India.png', 'Индонезия': 'Flag_Indonesia.png'}
Europe = {'Россия': 'Flag_Russia.png', 'Германия': 'Flag_Germany.png', 'Италия': 'Flag_Itali.png', 'Казахстан': 'Flag_Kazahstan.png'}

random_country_rus = random.choice(list(Europe.keys()) + list(Asia.keys()) + list(America.keys()))
random_country_eng = ""

if random_country_rus in Europe:
    random_country_eng = Europe[random_country_rus]
elif random_country_rus in Asia:
    random_country_eng = Asia[random_country_rus]
else:
    random_country_eng = America[random_country_rus]

new_random_countries_rus = random.sample(list(Europe.keys()) + list(Asia.keys()) + list(America.keys()), k=3)
while random_country_rus in new_random_countries_rus:
    new_random_countries_rus = random.sample(list(Europe.keys()) + list(Asia.keys()) + list(America.keys()), k=3)

random_countries_rus = new_random_countries_rus + [random_country_rus]
# перемешиваем список
random.shuffle(random_countries_rus)

# print('Название флага:')
# print(random_country_eng)
# print('Варианты ответа')
# print(', '.join(random_countries_rus))

pygame.init()

window_width, window_height = (800, 600)
# Создание экрана
screen = pygame.display.set_mode((window_width, window_height))

# Загрузка изображений
flag = pygame.transform.scale(load_image(random_country_eng), (window_width, window_height))
flag_rect = flag.get_rect()

# Загрузка шрифта
font = pygame.font.Font(None, 36)

# Создание кнопок
button1 = pygame.Rect(100, 200, 200, 50)
button2 = pygame.Rect(100, 300, 200, 50)
button3 = pygame.Rect(500, 200, 200, 50)
button4 = pygame.Rect(500, 300, 200, 50)

color_button1 = 'brown'
color_button2 = 'brown'
color_button3 = 'brown'
color_button4 = 'brown'

# Названия кнопок
button1_text = font.render(random_countries_rus[0], True, 'black')
button2_text = font.render(random_countries_rus[1], True, 'black')
button3_text = font.render(random_countries_rus[2], True, 'black')
button4_text = font.render(random_countries_rus[3], True, 'black')

# Переменная для хранения правильной кнопки
correct_button = None

# Главный цикл программы
running = True
while running:
    # Отрисовка экрана
    screen.fill('white')
    screen.blit(flag, flag_rect)

    # Отрисовка кнопок
    pygame.draw.rect(screen, 'green' if correct_button == button1_text else color_button1, button1)
    pygame.draw.rect(screen, 'green' if correct_button == button2_text else color_button2, button2)
    pygame.draw.rect(screen, 'green' if correct_button == button3_text else color_button3, button3)
    pygame.draw.rect(screen, 'green' if correct_button == button4_text else color_button4, button4)

    # Отрисовка текста на кнопках
    screen.blit(button1_text, (button1.x + 10, button1.y + 10))
    screen.blit(button2_text, (button2.x + 10, button2.y + 10))
    screen.blit(button3_text, (button3.x + 10, button3.y + 10))
    screen.blit(button4_text, (button4.x + 10, button4.y + 10))

    # Обработка события нажатия кнопки мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
# Проверка, на какую кнопку нажал пользователь
            if button1.collidepoint(mouse_pos):
                if random_countries_rus[0] == random_country_rus:
                    correct_button = button1_text
                elif color_button1 == 'red':
                    color_button1 = 'brown'
                else:
                    correct_button = None
                    color_button1 = 'red'
            elif button2.collidepoint(mouse_pos):
                if random_countries_rus[1] == random_country_rus:
                    correct_button = button2_text
                elif color_button2 == 'red':
                    color_button2 = 'brown'
                else:
                    correct_button = None
                    color_button2 = 'red'
            elif button3.collidepoint(mouse_pos):
                if random_countries_rus[2] == random_country_rus:
                    correct_button = button3_text
                elif color_button3 == 'red':
                    color_button3 = 'brown'
                else:
                    correct_button = None
                    color_button3 = 'red'
            elif button4.collidepoint(mouse_pos):
                if random_countries_rus[3] == random_country_rus:
                    correct_button = button4_text
                elif color_button4 == 'red':
                    color_button4 = 'brown'
                else:
                    correct_button = None
                    color_button4 = 'red'

    pygame.display.update()

pygame.quit()