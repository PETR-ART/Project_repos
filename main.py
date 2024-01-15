import random
import sys
import pygame
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


# количество раундов
N = 10

# словари со странами
America = {'США': 'USA', 'Канада': 'Canada', 'Мексика': 'Mexico', 'Куба': 'Cuba'}
Asia = {'Япония': 'Japan', 'Китай': 'China', 'Индия': 'India', 'Индонезия': 'Indonesia'}
Europe = {'Россия': 'Russia', 'Германия': 'Germany', 'Италия': 'Itali', 'Казахстан': 'Kazahstan'}


def get_random_country_eng():
    # берём одну русскую страну
    random_country_rus = random.choice(list(Europe.keys()) + list(Asia.keys()) + list(America.keys()))
    random_country_eng = ""
    # и её английское название
    if random_country_rus in Europe:
        random_country_eng = Europe[random_country_rus]
    elif random_country_rus in Asia:
        random_country_eng = Asia[random_country_rus]
    else:
        random_country_eng = America[random_country_rus]
    # и ещё 3 страны для вариантов выбора
    new_random_countries_rus = random.sample(list(Europe.keys()) + list(Asia.keys()) + list(America.keys()), k=3)
    while random_country_rus in new_random_countries_rus:
        new_random_countries_rus = random.sample(list(Europe.keys()) + list(Asia.keys()) + list(America.keys()), k=3)
    # добавляем нашу страну к списку
    random_countries_rus = new_random_countries_rus + [random_country_rus]
    # и перемешиваем список
    random.shuffle(random_countries_rus)
    return random_country_eng, random_country_rus, random_countries_rus


pygame.init()

window_size = window_width, window_height = 800, 600
window = pygame.display.set_mode(window_size)

font = pygame.font.Font(None, 38)
font1 = pygame.font.Font(None, 60)

button_width, button_height = 100, 40
button_x = window_width // 2 - button_width // 2
button_start_y = window_height // 2 - button_height // 2 - 80
button_rating_y = window_height // 2 - button_height // 2
button_exit_y = window_height // 2 - button_height // 2 + 80

log_width = window_width // 2
log_height = window_height - (window_height - 100)
input_width = window_width * 0.2
input1_width = (window_width - input_width) // 2
input_height = window_height * 0.4

start_image = pygame.transform.scale(load_image('start_image.jpg'), window_size)
first_image = pygame.transform.scale(load_image('first_image.webp'), window_size)
America_image = pygame.transform.scale(load_image('America.jpg'), window_size)
Europe_image = pygame.transform.scale(load_image('Europe.jpg'), window_size)
Asia_image = pygame.transform.scale(load_image('Asia.jpg'), window_size)
player_image = pygame.transform.scale(load_image('player.png'), window_size)


def Menu():
    pygame.display.set_caption("Меню")
    window.blit(start_image, (0, 0))

    pygame.draw.rect(window, 'brown', (button_x, button_start_y, button_width, button_height))
    pygame.draw.rect(window, 'brown', (button_x, button_rating_y, button_width, button_height))
    pygame.draw.rect(window, 'brown', (button_x, button_exit_y, button_width, button_height))

    font = pygame.font.Font(None, 38)
    text_start = font.render("Старт", True, 'white')
    text_rating = font.render("Рейтинг", True, 'white')
    text_exit = font.render("Выход", True, 'white')

    window.blit(text_start, (button_x + button_width // 2 - text_start.get_width() // 2,
                             button_start_y + button_height // 2 - text_start.get_height() // 2))
    window.blit(text_rating, (button_x + button_width // 2 - text_rating.get_width() // 2,
                              button_rating_y + button_height // 2 - text_rating.get_height() // 2))
    window.blit(text_exit, (button_x + button_width // 2 - text_exit.get_width() // 2,
                            button_exit_y + button_height // 2 - text_exit.get_height() // 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # print((mouse_x, mouse_y))
                if button_x <= mouse_x <= button_x + button_width:
                    if button_start_y <= mouse_y <= button_start_y + button_height:
                        Start()
                    elif button_rating_y <= mouse_y <= button_rating_y + button_height:
                        Rating()
                    elif button_exit_y <= mouse_y <= button_exit_y + button_height:
                        pygame.quit()
                        sys.exit()
        pygame.display.flip()


def Start():
    pygame.display.set_caption("Инициализация")

    window.blit(first_image, (0, 0))

    text_log = font.render('Введите логин', True, 'Brown')
    window.blit(text_log, (log_width - 90, log_height - 10, log_width, log_height))

    pygame.draw.rect(window, 'brown', (input_width, input_height,  window_width - input1_width, 100))

    pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y - 5, button_width + 80, button_height + 5))
    text_continue = font.render("Продолжить", True, 'white')
    window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                    button_exit_y + button_height // 2 - text_continue.get_height() // 2))

    pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 65, button_width + 80, button_height + 5))
    text_back = font.render("Назад", True, 'white')
    window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                            button_exit_y + button_height // 2 - text_back.get_height() // 2 + 70))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # print((mouse_x, mouse_y))
                if 310 <= mouse_x <= 490 and 355 <= mouse_y <= 400:
                    Check_setting()
                if 310 <= mouse_x <= 490 and 425 <= mouse_y <= 470:
                    Menu()

        pygame.display.flip()


def Rating():
    pygame.display.set_caption("Рейтинг")

    window.blit(first_image, (0, 0))

    text_check = font.render('Рекорды', True, 'Brown')
    window.blit(text_check, (350, 60, 400, 80))

    pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 125, button_width + 80, button_height + 5))
    text_back = font.render("Назад", True, 'white')
    window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                            button_exit_y + button_height // 2 - text_back.get_height() // 2 + 130))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # print((mouse_x, mouse_y))
                if 310 <= mouse_x <= 490 and 485 <= mouse_y <= 530:
                    Menu()
        pygame.display.flip()


def Check_setting():
    # Флаги Настроек Стран
    Europe = False
    America = False
    Asia = False

    # Флаги Цвета Кнопок У Стран
    Europe_color = 'brown'
    America_color = 'brown'
    Asia_color = 'brown'

    # Флаги Настроек Режима
    mod_towns = False
    mod_flag = False

    # Флаги Цвета Кнопок У Настроек Режима
    Flags_color = 'brown'
    Town_color = 'brown'

    # Отображение заголовка
    pygame.display.set_caption("Выбор Режима")
    window.blit(first_image, (0, 0))

    # Отображение текста "Выберите режим"
    text_check = font.render('Выберите режим', True, 'Brown')
    window.blit(text_check, (310, 60, 400, 80))

    while True:
        # Отображение кнопок
        pygame.draw.rect(window, Europe_color,
                         (button_x - 250, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Европа", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 210,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, America_color,
                         (button_x - 50, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Америка", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 10,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, Asia_color,
                         (button_x + 150, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Азия", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 + 190,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, Flags_color,
                         (button_x - 200, button_exit_y - 120, button_width + 80, button_height + 5))
        text_europe = font.render("Флаги", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 160,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 118))

        pygame.draw.rect(window, Town_color,
                         (button_x + 80, button_exit_y - 120, button_width + 80, button_height + 5))
        text_europe = font.render("Города", True, 'white')
        window.blit(text_europe, (button_x + 15 + button_width // 2 - text_europe.get_width() // 2 + 100,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 118))

        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 55, button_width + 80, button_height + 5))
        text_continue = font.render("Продолжить", True, 'white')
        window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                    button_exit_y + button_height // 2 - text_continue.get_height() // 2 + 60))

        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 125, button_width + 80, button_height + 5))
        text_back = font.render("Назад", True, 'white')
        window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                                button_exit_y + button_height // 2 - text_back.get_height() // 2 + 130))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))
                if 310 <= mouse_x <= 490 and 485 <= mouse_y <= 530:
                    Start()

                if 100 <= mouse_x <= 280 and 140 <= mouse_y <= 180:
                    if Europe:
                        Europe_color = 'brown'
                        Europe = False
                    else:
                        Europe_color = 'red'
                        Europe = True

                if 300 <= mouse_x <= 480 and 140 <= mouse_y <= 180:
                    if America:
                        America_color = 'brown'
                        America = False
                    else:
                        America_color = 'red'
                        America = True

                if 500 <= mouse_x <= 680 and 140 <= mouse_y <= 180:
                    if Asia:
                        Asia_color = 'brown'
                        Asia = False
                    else:
                        Asia_color = 'red'
                        Asia = True

                if 150 <= mouse_x <= 320 and 240 <= mouse_y <= 280:
                    if mod_flag:
                        Flags_color = 'brown'
                        mod_flag = False
                    else:
                        Flags_color = 'red'
                        mod_flag = True

                if 430 <= mouse_x <= 640 and 240 <= mouse_y <= 280:
                    if mod_towns:
                        Town_color = 'brown'
                        mod_towns = False
                    else:
                        Town_color = 'red'
                        mod_towns = True

                if 300 <= mouse_x <= 480 and 410 <= mouse_y <= 450:
                    tip = ''
                    if mod_towns and not mod_flag:
                        tip = 'towns'
                    if mod_flag and not mod_towns:
                        tip = 'flag'
                    if Europe:
                        if tip != '':
                            Game_Europe(tip)
                    if America:
                        if tip != '':
                            Game_America(tip)
                    if Asia:
                        if tip != '':
                            Game_Asia(tip)
        pygame.display.flip()


def Game_America(tip):
    pygame.display.set_caption('Игра')
    window.blit(America_image, (0, 0))

    if tip == 'towns':
        pass
    if tip == 'flag':
        pass

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))

        pygame.display.flip()


def Game_Asia(tip):
    pygame.display.set_caption('Игра')
    window.blit(Asia_image, (0, 0))

    if tip == 'towns':
        pass
    if tip == 'flag':
        pass

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))

        pygame.display.flip()


def Game_Europe(tip):
    pygame.display.set_caption('Игра')
    window.blit(Europe_image, (0, 0))

    if tip == 'towns':
        town_color = 'brown'
        pygame.draw.circle(window, town_color, (350, 464), 4)  # Рим
        pygame.draw.circle(window, town_color, (359, 529), 4)  # Палермо
        pygame.draw.circle(window, town_color, (355, 407), 4)  # Венеция
        pygame.draw.circle(window, town_color, (542, 475), 4)  # Стамбул
        pygame.draw.circle(window, town_color, (243, 296), 4)  # Лондон
        pygame.draw.circle(window, town_color, (220, 453), 4)  # Барселона
        pygame.draw.circle(window, town_color, (113, 491), 4)  # Севилья
        pygame.draw.circle(window, town_color, (484, 527), 4)  # Афины
        pygame.draw.circle(window, town_color, (407, 371), 4)  # Братислава
        pygame.draw.circle(window, town_color, (381, 341), 4)  # Прага
        pygame.draw.circle(window, town_color, (366, 248), 4)  # Копенгаген
        pygame.draw.circle(window, town_color, (354, 188), 4)  # Осло
        pygame.draw.circle(window, town_color, (474, 233), 4)  # Рига
        pygame.draw.circle(window, town_color, (479, 196), 4)  # Таллин
        pygame.draw.circle(window, town_color, (484, 266), 4)  # Вильнюс
        pygame.draw.circle(window, town_color, (522, 183), 4)  # Санкт-Петербург
        pygame.draw.circle(window, town_color, (430, 387), 4)  # Будапешт
        pygame.draw.circle(window, town_color, (83, 456), 4)  # Лиссабон
        pygame.draw.circle(window, town_color, (306, 379), 4)  # Берн
        pygame.draw.circle(window, town_color, (286, 385), 4)  # Женева
        pygame.draw.circle(window, town_color, (288, 293), 4)  # Амстердам
    if tip == 'flag':
        pass
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))

        pygame.display.flip()


def end(res_game):
    pygame.display.set_caption('Конец игры')
    window.blit(first_image, (0, 0))
    text_res = font1.render(res_game, True, 'Brown')
    window.blit(text_res, (320, 100))
    text_go = font.render('Для продолжения нажмите на любую клавишу', True, 'Brown')
    window.blit(text_go, (70, 150))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                Menu()
        pygame.display.flip()


running = True
Menu()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
