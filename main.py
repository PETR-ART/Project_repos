import random
import sys
import pygame
import os

# Словари с городами
towns_europe = {'Рим': '350, 464', 'Палермо': '359, 529', 'Венеция': '355, 407', 'Стамбул': '542, 475',
                'Лондон': '243, 296', 'Барселона': '220, 453', 'Севилья': '113, 491', 'Афины': '484, 527',
                'Братислава': '407, 371', 'Прага': '381, 341', 'Копенгаген': '366, 248', 'Осло': '354, 188',
                'Рига': '474, 233', 'Таллин': '479, 196', 'Вильнюс': '484, 266', 'Санкт-Петербург': '522, 183',
                'Будапешт': '430, 387', 'Лиссабон': '83, 456', 'Берн': '306, 379', 'Женева': '286, 385',
                'Амстердам': '288, 293', 'Мадрид': '151, 456', 'Париж': '258, 346', 'Брюссель': '281, 318',
                'Берлин': '365, 300', 'Варшава': '437, 309', 'Рейкьявик': '137, 48', 'Вена': '397, 373',
                'Любляна': '379, 404', 'Дублин': '188, 252', 'Москва': '632, 246', 'Архангельск': '588, 98',
                'Минск': '513, 282', 'Киев': '546, 325', 'Стокгольм': '412, 200', 'Хельсинки': '482, 179',
                'Севастополь': '589, 416', 'Кишнёв': '529, 382', 'Бухарест': '508, 426', 'София': '477, 457',
                'Белград': '447, 430', 'Скопье': '455, 473', 'Тирана': '435, 483', 'Калининград': '438, 267',
                'Подгорица': '428, 460', 'Загреб': '392, 406', 'Сараево': '419, 439', 'Сочи': '654, 409',
                'Бордо': '208, 392', 'Кардиф': '206, 281', 'Эдинбург': '229, 218', 'Ла Корунья': '113, 391',
                'Гамбург': '340, 283', 'Франкфурт': '316, 332', 'Мюнхен': '347, 367', 'Брно': '403, 351',
                'Данциг': '426, 276', 'Великий Новгород': '539, 212', 'Ростов на Дону': '644, 360', 'Порту': '101, 424',
                'Брест': '473, 309', 'Львов': '485, 357', 'Одесса': '556, 387', 'Турин': '301, 410', 'Милан': '323, 406',
                'Неаполь': '375, 485', 'Люксембург': '295, 335', 'Монако': '288, 430', 'Сан - Марино': '349, 433',
                'Варна': '523, 454', 'Мурманск': '523, 51', 'Петрозаводск': '556, 156'}


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


def get_random_towns(tip):
    if tip == 'Europe':
        random_town = random.choice(list(towns_europe))
        random_town_cords = towns_europe[random_town]
        return random_town, random_town_cords


get_random_towns('Europe')

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
    mod_eng = False

    # Флаги Цвета Кнопок У Настроек Режима
    Flags_color = 'brown'
    Town_color = 'brown'
    Eng_color = 'brown'

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

        pygame.draw.rect(window, Eng_color,
                         (button_x - 120, button_exit_y - 40, button_width + 200, button_height + 5))
        text_europe = font.render("Английские Названия", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 20,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 38))

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

                if 230 <= mouse_x <= 530 and 320 <= mouse_y <= 360:
                    if mod_eng:
                        Eng_color = 'brown'
                        mod_eng = False
                    else:
                        Eng_color = 'red'
                        mod_eng = True

                if 300 <= mouse_x <= 480 and 410 <= mouse_y <= 450:
                    if Europe and mod_towns:
                        Game_Europe()
                    if America and mod_towns:
                        Game_America()
                    if Asia and mod_towns:
                        Game_Asia()
                    tip1 = []
                    tip2 = []
                    if Europe:
                        tip1.append('Europe')
                    if America:
                        tip1.append('America')
                    if Asia:
                        tip1.append('Asia')
                    if mod_eng:
                        tip2.append('mod_eng')
                    if mod_flag:
                        tip2.append('mod_flag')
                    Game(tip1, tip2)

        pygame.display.flip()


def Game(tip1, tip2):
    pygame.display.set_caption('Игра')
    # количество раундов
    n = 10
    clock = pygame.time.Clock()
    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1500)

    # Загрузка шрифта
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 60)

    # Создание кнопок
    button1 = pygame.Rect(100, 200, 200, 50)
    button2 = pygame.Rect(100, 300, 200, 50)
    button3 = pygame.Rect(500, 200, 200, 50)
    button4 = pygame.Rect(500, 300, 200, 50)

    # Переменная для хранения правильной кнопки
    correct_button = None
    wrong_button = None
    is_wrong_answer = False

    # Главный цикл программы
    new_round = True
    running = True
    while running and n != -1:
        if new_round:
            n -= 1
            counter, text = 11, str(counter).rjust(3)
            choice = random.choice([0, 1])
            random_country_eng, random_country_rus, random_countries_rus = get_random_country_eng()
            correct_button = None
            wrong_button = None
            is_wrong_answer = False
            new_round = False

        if n == -1:
            end(res_game='Victory')

        window.fill('white')
        if 'mod_flag' in tip2 and 'mod_eng' not in tip2:
            flag = pygame.transform.scale(pygame.image.load('image\Flag_' + random_country_eng + '.png'),
                                          (window_width, window_height))
            flag_rect = flag.get_rect()
            window.blit(flag, flag_rect)
        elif 'mod_flag' not in tip2 and 'mod_eng' in tip2:
            country_eng = font1.render(random_country_eng, True, 'black')
            window.blit(country_eng, (window_width / 2 - 60, 50))
        else:
            if choice:
                flag = pygame.transform.scale(pygame.image.load('image\Flag_' + random_country_eng + '.png'),
                                              (window_width, window_height))
                flag_rect = flag.get_rect()
                window.blit(flag, flag_rect)
            else:
                country_eng = font1.render(random_country_eng, True, 'black')
                window.blit(country_eng, (window_width / 2 - 60, 50))

        button1_text = font.render(random_countries_rus[0], True, 'black')
        button2_text = font.render(random_countries_rus[1], True, 'black')
        button3_text = font.render(random_countries_rus[2], True, 'black')
        button4_text = font.render(random_countries_rus[3], True, 'black')

        pygame.draw.rect(window, 'green' if correct_button == button1_text else 'brown', button1)
        pygame.draw.rect(window, 'green' if correct_button == button2_text else 'brown', button2)
        pygame.draw.rect(window, 'green' if correct_button == button3_text else 'brown', button3)
        pygame.draw.rect(window, 'green' if correct_button == button4_text else 'brown', button4)

        window.blit(button1_text, (button1.x + 10, button1.y + 10))
        window.blit(button2_text, (button2.x + 10, button2.y + 10))
        window.blit(button3_text, (button3.x + 10, button3.y + 10))
        window.blit(button4_text, (button4.x + 10, button4.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    end(res_game='Game over')
                is_wrong_answer = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button1.collidepoint(mouse_pos):
                    if random_countries_rus[0] == random_country_rus:
                        correct_button = button1_text
                        new_round = True
                    else:
                        wrong_button = button1_text
                        is_wrong_answer = True
                elif button2.collidepoint(mouse_pos):
                    if random_countries_rus[1] == random_country_rus:
                        correct_button = button2_text
                        new_round = True
                    else:
                        wrong_button = button2_text
                        is_wrong_answer = True
                elif button3.collidepoint(mouse_pos):
                    if random_countries_rus[2] == random_country_rus:
                        correct_button = button3_text
                        new_round = True
                    else:
                        wrong_button = button3_text
                        is_wrong_answer = True
                elif button4.collidepoint(mouse_pos):
                    if random_countries_rus[3] == random_country_rus:
                        correct_button = button4_text
                        new_round = True
                    else:
                        wrong_button = button4_text
                        is_wrong_answer = True
            if is_wrong_answer:
                if wrong_button:
                    if counter > 5:
                        counter -= 5
                        text = str(counter).rjust(3)
                    else:
                        counter = 0
                        text = str(counter).rjust(3)
                    is_wrong_answer = False

        pygame.draw.rect(window, 'grey', (720, 0, 800, 40))
        window.blit(font.render(text, True, (0, 0, 0)), (720, 10))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)


def Game_America():
    tip = 'America'
    pygame.display.set_caption('Игра')
    window.blit(America_image, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))

        pygame.display.flip()


def Game_Asia():
    tip = 'Asia'
    pygame.display.set_caption('Игра')
    window.blit(Asia_image, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))

        pygame.display.flip()


def Game_Europe():
    kol = 0
    tip = 'Europe'
    pygame.display.set_caption('Игра')
    window.blit(Europe_image, (0, 0))

    pygame.draw.rect(window, 'grey', (570, 440, 230, 150))

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
    pygame.draw.circle(window, town_color, (151, 456), 4)  # Мадрид
    pygame.draw.circle(window, town_color, (258, 346), 4)  # Париж
    pygame.draw.circle(window, town_color, (281, 318), 4)  # Брюссель
    pygame.draw.circle(window, town_color, (365, 300), 4)  # Берлин
    pygame.draw.circle(window, town_color, (437, 309), 4)  # Варшава
    pygame.draw.circle(window, town_color, (137, 48), 4)  # Рейкьявик
    pygame.draw.circle(window, town_color, (397, 373), 4)  # Вена
    pygame.draw.circle(window, town_color, (379, 404), 4)  # Любляна
    pygame.draw.circle(window, town_color, (188, 252), 4)  # Дублин
    pygame.draw.circle(window, town_color, (632, 246), 4)  # Москва
    pygame.draw.circle(window, town_color, (588, 98), 4)  # Архангельск
    pygame.draw.circle(window, town_color, (513, 282), 4)  # Минск
    pygame.draw.circle(window, town_color, (546, 325), 4)  # Киев
    pygame.draw.circle(window, town_color, (412, 200), 4)  # Стокгольм
    pygame.draw.circle(window, town_color, (482, 179), 4)  # Хельсинки
    pygame.draw.circle(window, town_color, (589, 416), 4)  # Севастополь
    pygame.draw.circle(window, town_color, (529, 382), 4)  # Кишнёв
    pygame.draw.circle(window, town_color, (508, 426), 4)  # Бухарест
    pygame.draw.circle(window, town_color, (477, 457), 4)  # София
    pygame.draw.circle(window, town_color, (447, 430), 4)  # Белград
    pygame.draw.circle(window, town_color, (455, 473), 4)  # Скопье
    pygame.draw.circle(window, town_color, (435, 483), 4)  # Тирана
    pygame.draw.circle(window, town_color, (438, 267), 4)  # Калининград
    pygame.draw.circle(window, town_color, (428, 460), 4)  # Подгорица
    pygame.draw.circle(window, town_color, (392, 406), 4)  # Загреб
    pygame.draw.circle(window, town_color, (419, 439), 4)  # Сараево
    pygame.draw.circle(window, town_color, (654, 409), 4)  # Сочи
    pygame.draw.circle(window, town_color, (208, 392), 4)  # Бордо
    pygame.draw.circle(window, town_color, (206, 281), 4)  # Кардиф
    pygame.draw.circle(window, town_color, (229, 218), 4)  # Эдинбург
    pygame.draw.circle(window, town_color, (113, 391), 4)  # Ла Корунья
    pygame.draw.circle(window, town_color, (340, 283), 4)  # Гамбург
    pygame.draw.circle(window, town_color, (316, 332), 4)  # Франкфурт
    pygame.draw.circle(window, town_color, (347, 367), 4)  # Мюнхен
    pygame.draw.circle(window, town_color, (403, 351), 4)  # Брно
    pygame.draw.circle(window, town_color, (426, 276), 4)  # Данциг
    pygame.draw.circle(window, town_color, (539, 212), 4)  # Великий Новгород
    pygame.draw.circle(window, town_color, (644, 360), 4)  # Ростов на Дону
    pygame.draw.circle(window, town_color, (101, 424), 4)  # Порту
    pygame.draw.circle(window, town_color, (473, 309), 4)  # Брест
    pygame.draw.circle(window, town_color, (485, 357), 4)  # Львов
    pygame.draw.circle(window, town_color, (556, 387), 4)  # Одесса
    pygame.draw.circle(window, town_color, (301, 410), 4)  # Турин
    pygame.draw.circle(window, town_color, (323, 406), 4)  # Милан
    pygame.draw.circle(window, town_color, (375, 485), 4)  # Неаполь
    pygame.draw.circle(window, town_color, (295, 335), 4)  # Люксембург
    pygame.draw.circle(window, town_color, (288, 430), 4)  # Монако
    pygame.draw.circle(window, town_color, (349, 433), 4)  # Сан-Марино
    pygame.draw.circle(window, town_color, (523, 454), 4)  # Варна
    pygame.draw.circle(window, town_color, (523, 51), 4)  # Мурманск
    pygame.draw.circle(window, town_color, (556, 156), 4)  # Петрозаводск
    pygame.display.flip()

    used_towns = []
    town_and_cords = get_random_towns('Europe')
    cords = town_and_cords[1].split(', ')
    print(town_and_cords[0], town_and_cords[1][:3], town_and_cords[1][-3:])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))
                if abs(mouse_x - int(cords[0])) < 5 and abs(mouse_y - int(cords[1])) < 5:
                    kol += 1
                    print(kol)
                    used_towns.append(town_and_cords[0])
                    pygame.draw.circle(window,'green', (int(cords[0]), int(cords[1])), 4)
                town_and_cords = get_random_towns('Europe')
                cords = town_and_cords[1].split(', ')
                if town_and_cords[0] in used_towns:
                    print(1)
                    town_and_cords = get_random_towns('Europe')
                print(town_and_cords[0], cords[0], cords[1])

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
