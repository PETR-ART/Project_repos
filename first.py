import random
import sys
import pygame
import os


# словари со странами
America = {'США': 'USA', 'Канада': 'Canada', 'Мексика': 'Mexico', 'Куба': 'Cuba'}
Asia = {'Япония': 'Japan', 'Китай': 'China', 'Индия': 'India', 'Индонезия': 'Indonesia'}
Europe = {'Россия': 'Russia', 'Германия': 'Germany', 'Италия': 'Itali', 'Казахстан': 'Kazahstan'}


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
Player_image = pygame.transform.scale(load_image('player.png'), window_size)


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
    mod_eng = False
    mod_flag = False

    # Флаги Цвета Кнопок У Настроек Режима
    Flags_color = 'brown'
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

        pygame.draw.rect(window, Eng_color,
                         (button_x, button_exit_y - 120, button_width + 200, button_height + 5))
        text_europe = font.render("Английские Названия", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 + 100,
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
                # print((mouse_x, mouse_y))
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

                if 350 <= mouse_x <= 640 and 240 <= mouse_y <= 280:
                    if mod_eng:
                        Eng_color = 'brown'
                        mod_eng = False
                    else:
                        Eng_color = 'red'
                        mod_eng = True

                if 300 <= mouse_x <= 480 and 410 <= mouse_y <= 450:
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


# Будующие спрайты
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

running = True
Menu()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # В процессе
    tiles_group.draw(window)
    player_group.draw(window)
    pygame.display.flip()
