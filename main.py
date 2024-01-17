import sqlite3
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

towns_America = {'Вашингтон': '458, 254', 'Нью - Йорк': '472, 246', 'Бостон': '487, 239', 'Майами': '437, 302',
                 'Новый Орлеан': '393, 289', 'Гавана': '432, 312', 'Лос-Анджелес': '253, 272',
                 'Сан-Франциско': '241, 259', 'Ванкувер': '235, 212', 'Галифакс': '520, 232', 'Квебек': '489, 220',
                 'Торонто': '444, 235', 'Виннипег': '356, 208', 'Даллас': '352, 277', 'Канзас-Сити': '372, 256',
                 'Анкоридж': '108, 158', 'Сиэтл': '239, 221', 'Хьюстон': '362, 292', 'Гуантанамо': '460, 322',
                 'Санто-Доминго': '487, 326', 'Кингстон': '454, 328', 'Джексонвилл': '432, 281', 'Шарлотт': '436, 266',
                 'Атланта': '419, 274', 'Гуаякиль': '445, 395', 'Богота': '464, 366', 'Каракас': '501, 353',
                 'Джорджтаун': '545, 368', 'Парамарибо': '557, 370', 'Панама': '444, 357', 'Гватемала': '391, 337',
                 'Манагуа': '412, 348', 'Сан-Хосе': '423, 355', 'Кито': '449, 385', 'Лима': '459, 428',
                 'Ла-Пас': '498, 436', 'Асуньсьон': '548, 468', 'Буэнос-Айрес': '548, 504', 'Монтевидео': '555, 501',
                 'Антофагаста': '489, 464', 'Сантьяго': '486, 500', 'Кордова': '509, 499', 'Нуук': '578, 143',
                 'Оттава': '472, 228', 'Мехико': '345, 320', 'Лас-Вегас': '265, 259', 'Солт-Лейк-Сити': '273, 247',
                 'Денвер': '310, 255', 'Монтерей': '343, 300', 'Сьюдад-Хуарес': '312, 281', 'Эрмосильо': '301, 295',
                 'Мерида': '398, 318', 'Белен': '592, 393', 'Сан-Луис': '613, 398'}

towns_Asia = {'Стамбул': '28, 267', 'Анкара': '44, 279', 'Анталья': '38, 293', 'Трабзон': '82, 269',
              'Тбилиси': '101, 265', 'Ереван': '106, 277', 'Баку': '128, 272', 'Дамаск': '70, 312', 'Алеппо': '72, 300',
              'Мосул': '98, 301', 'Багдад': '103, 320', 'Кувейт': '117, 339', 'Медина': '81, 369', 'Мекка': '79, 386',
              'Сана': '101, 425', 'Аден': '109, 439', 'Маскат': '171, 378', 'Абу-Даби': '148, 372',
              'Тебриз': '111, 289', 'Шираз': '149, 346', 'Тегеран': '135, 304', 'Мешхед': '172, 298',
              'Герат': '187, 312', 'Ашхабад': '172, 287', 'Самарканд': '214, 275', 'Ташкент': '223, 269',
              'Душанбе': '219, 284', 'Эр-Рияд': '117, 366', 'Алматы': '257, 253', 'Бишкек': '247, 258',
              'Астана': '232, 206', 'Караганда': '240, 215', 'Кабул': '219, 304', 'Кандагар': '204, 322',
              'Исламабад': '236, 315', 'Карачи': '210, 363', 'Лахор': '241, 326', 'Нью-Дели': '262, 342',
              'Мумбаи': '241, 406', 'Катманду': '297, 353', 'Дакка': '321, 376', 'Тхимпху': '319, 355',
              'Коломбо': '272, 474', 'Мадурай': '264, 460', 'Хайдарабад': '264, 414', 'Калькутта': '310, 385',
              'Амман': '62, 326', 'Мандалай': '346, 386', 'Бангкок': '369, 436', 'Ханой': '395, 388',
              'Пном Пен': '391, 448', 'Хошимин': '397, 457', 'Куала-Лумпур': '375, 503', 'Сингапур': '388, 515',
              'Медан': '365, 502', 'Джакарта': '403, 559', 'Бруней': '436, 496', 'Кучинг': '421, 511',
              'Давао': '490, 478', 'Манила': '467, 433', 'Тайбэй': '470, 366', 'Гонконг': '434, 383',
              'Шанхай': '464, 332', 'Пекин': '447, 279', 'Ухань': '424, 332', 'Сиань': '393, 312', 'Чунцин': '391, 342',
              'Пхеньян': '492, 281', 'Сеул': '496, 292', 'Харбин': '490 , 239', 'Улан-Батор': '396, 227',
              'Владивосток': '526, 255', 'Куньмин': '377, 364', 'Токио': '558, 300', 'Осака': '537, 306',
              ' Фукуока': '513, 316', 'Красноярск': '338, 167', 'Омск': '240, 175', 'Иркутск': '385, 198',
              'Саппоро': '566, 256', 'Цзинань': '444, 296'}

conn = sqlite3.connect("comandproject.db")
cursor = conn.cursor()

# Функция для проверки наличия логина в базе данных
def check_login(login):
    cursor.execute("SELECT * FROM setting WHERE login=?", (login,))
    result = cursor.fetchone()
    conn.close()
    return bool(result)


# Функция для проверки правильности пароля
def check_password(login, password):
    cursor.execute("SELECT password FROM setting WHERE login=?", (login,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0] == password
    return False


# Функция для добавления пользователя в базу данных
def register(login, password):
    cursor.execute("INSERT INTO setting VALUES (?, ?, '', '', '')", (login, password))
    conn.commit()
    conn.close()


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
    if tip == 'America':
        random_town = random.choice(list(towns_America))
        random_town_cords = towns_America[random_town]
        return random_town, random_town_cords
    if tip == 'Asia':
        random_town = random.choice(list(towns_Asia))
        random_town_cords = towns_Asia[random_town]
        return random_town, random_town_cords


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

    button_enter = pygame.Rect(log_width - 185, log_height + 100, log_width / 2 - 35, log_height - 50)
    pygame.draw.rect(window, 'brown', button_enter)

    text_enter = font.render('Вход', True, 'white')
    window.blit(text_enter, (log_width - 135, log_height + 110, log_width - 15, log_height - 50))

    button_register = pygame.Rect(log_width + 30, log_height + 100, log_width / 2 - 20, log_height - 50)
    pygame.draw.rect(window, 'brown', button_register)

    text_reg = font.render('Регистрация', True, 'white')
    window.blit(text_reg, (log_width + 35, log_height + 110, log_width, log_height - 50))

    button_next = pygame.Rect(button_x - 40, button_exit_y - 5, button_width + 80, button_height + 5)
    pygame.draw.rect(window, 'brown', button_next)

    text_continue = font.render("Продолжить", True, 'white')
    window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                button_exit_y + button_height // 2 - text_continue.get_height() // 2))

    button_back = pygame.Rect(button_x - 40, button_exit_y + 65, button_width + 80, button_height + 5)
    pygame.draw.rect(window, 'brown', button_back)

    text_back = font.render("Назад", True, 'white')
    window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                            button_exit_y + button_height // 2 - text_back.get_height() // 2 + 70))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if button_enter.collidepoint(mouse_pos):
                    Enter()

                if button_register.collidepoint(mouse_pos):
                    Register()

                if button_next.collidepoint(mouse_pos):
                    Check_setting()
                    login = input("Введите логин: ")
                    password = input("Введите пароль: ")
                    repeat_password = input("Повторите пароль: ")

                    if repeat_password == password and not check_login(login):
                        register(login, password)
                    else:
                        print("Ошибка при регистрации")

                if button_back.collidepoint(mouse_pos):
                    Menu()
                    login = input("Введите логин: ")
                    password = input("Введите пароль: ")

                    if check_login(login) and check_password(login, password):
                        Menu()
                    else:
                        print("Неверный логин или пароль")

        pygame.display.flip()



def Register():
    pygame.display.set_caption("Регистрация")
    window.blit(first_image, (0, 0))

    button_login = pygame.Rect(log_width - 150, log_height, log_width / 2 + 100, log_height - 50)
    pygame.draw.rect(window, 'brown', button_login)

    text_enter = font.render('Логин', True, 'dark grey')
    window.blit(text_enter, (log_width - 135, log_height + 110, log_width - 15, log_height - 100))

    button_password = pygame.Rect(log_width - 150, log_height + 100, log_width / 2 + 100, log_height - 50)
    pygame.draw.rect(window, 'brown', button_password)

    text_reg = font.render('Пароль', True, 'dark grey')
    window.blit(text_reg, (log_width + 35, log_height + 110, log_width, log_height - 50))

    button_next = pygame.Rect(button_x - 40, button_exit_y - 5, button_width + 80, button_height + 5)
    pygame.draw.rect(window, 'brown', button_next)

    text_continue = font.render("Продолжить", True, 'white')
    window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                button_exit_y + button_height // 2 - text_continue.get_height() // 2))

    button_back = pygame.Rect(button_x - 40, button_exit_y + 65, button_width + 80, button_height + 5)
    pygame.draw.rect(window, 'brown', button_back)

    text_back = font.render("Назад", True, 'white')
    window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                            button_exit_y + button_height // 2 - text_back.get_height() // 2 + 70))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if button_login.collidepoint(mouse_pos):
                    Enter()

                if button_password.collidepoint(mouse_pos):
                    Register()

                if button_next.collidepoint(mouse_pos):
                    Check_setting()
                    login = input("Введите логин: ")
                    password = input("Введите пароль: ")
                    repeat_password = input("Повторите пароль: ")

                    if repeat_password == password and not check_login(login):
                        register(login, password)
                    else:
                        print("Ошибка при регистрации")

                if button_back.collidepoint(mouse_pos):
                    Menu()
                    login = input("Введите логин: ")
                    password = input("Введите пароль: ")

                    if check_login(login) and check_password(login, password):
                        Menu()
                    else:
                        print("Неверный логин или пароль")

        pygame.display.flip()


def Enter():
    pass


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
                    if Europe and mod_towns and not Asia and not America and not mod_eng and not mod_flag:
                        Game_Europe()
                    if America and mod_towns and not Asia and not Europe and not mod_eng and not mod_flag:
                        Game_America()
                    if Asia and mod_towns and not America and not Europe and not mod_eng and not mod_flag:
                        Game_Asia()
                    tip1 = ''
                    tip2 = ''
                    if Europe:
                        tip1 = 'Europe'
                    if America:
                        tip1 = 'America'
                    if Asia:
                        tip1 = 'Asia'
                    if mod_eng and tip1 != '':
                        tip2 = 'mod_eng'
                        Game(tip1, tip2)
                    if mod_flag and tip1 != '':
                        tip2 = 'mod_flag'
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
            flag = pygame.transform.scale(pygame.image.load('data\images\Flag_' + random_country_eng + '.png'),
                                          (window_width, window_height))
            flag_rect = flag.get_rect()
            window.blit(flag, flag_rect)
        elif 'mod_flag' not in tip2 and 'mod_eng' in tip2:
            country_eng = font1.render(random_country_eng, True, 'black')
            window.blit(country_eng, (window_width / 2 - 60, 50))
        else:
            if choice:
                flag = pygame.transform.scale(pygame.image.load('data\images\Flag_' + random_country_eng + '.png'),
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


def draw_town(window, town_color, x, y):
    pygame.draw.circle(window, town_color, (x, y), 4)


def draw_all_towns(window, town_color, towns):
    for town in towns:
        draw_town(window, town_color, town[0], town[1])


def Game_America():
    kol = 0
    tip = 'America'
    pygame.display.set_caption('Игра')
    window.blit(America_image, (0, 0))

    pygame.draw.rect(window, 'grey', (560, 440, 230, 150))

    town_color = 'brown'
    towns = [(458, 254), (472, 246), (487, 239), (437, 302), (393, 289), (432, 312), (253, 272), (241, 259), (235, 212),
             (520, 232), (489, 220), (444, 235), (356, 208), (352, 277), (372, 256), (108, 158), (239, 221), (362, 292),
             (460, 322), (487, 326), (454, 328), (432, 281), (436, 266), (419, 274), (445, 395), (464, 366), (501, 353),
             (545, 368), (557, 370), (444, 357), (391, 337), (412, 348), (423, 355), (449, 385), (459, 428), (498, 436),
             (548, 468), (548, 504), (555, 501), (489, 464), (486, 500), (509, 499), (578, 143), (472, 228), (345, 320),
             (265, 259), (273, 247), (310, 255), (343, 300), (312, 281), (301, 295), (398, 318), (592, 393), (613, 398)]
    draw_all_towns(window, town_color, towns)
    pygame.display.flip()

    used_towns = []
    town_and_cords = get_random_towns('America')
    cords = town_and_cords[1].split(', ')

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
                    used_towns.append(town_and_cords[0])
                    pygame.draw.circle(window, 'green', (int(cords[0]), int(cords[1])), 4)
                town_and_cords = get_random_towns('America')
                cords = town_and_cords[1].split(', ')
                while True:
                    if town_and_cords[0] in used_towns:
                        town_and_cords = get_random_towns('America')
                        cords = town_and_cords[1].split(', ')
                    else:
                        break

            pygame.draw.rect(window, 'grey', (560, 440, 230, 150))
            text_town = font.render(town_and_cords[0], True, 'black')
            window.blit(text_town, (560, 450))
            text_kol = font.render(('Счёт:' + str(kol)), True, 'black')
            window.blit(text_kol, (560, 500))
        pygame.display.flip()


def Game_Asia():
    kol = 0
    tip = 'Asia'
    pygame.display.set_caption('Игра')
    window.blit(Asia_image, (0, 0))

    pygame.draw.rect(window, 'grey', (560, 440, 230, 150))

    town_color = 'brown'
    towns = [(28, 267), (44, 279), (38, 293), (82, 269), (101, 265), (106, 277), (128, 272), (70, 312), (72, 300),
             (98, 301), (103, 320), (117, 339), (81, 369), (79, 386), (101, 425), (109, 439), (171, 378), (148, 372),
             (111, 289), (149, 346), (135, 304), (172, 298), (187, 312), (172, 287), (214, 275), (223, 269), (219, 284),
             (117, 366), (257, 253), (247, 258), (232, 206), (240, 215), (219, 304), (204, 322), (236, 315), (210, 363),
             (241, 326), (262, 342), (241, 406), (297, 353), (321, 376), (319, 355), (272, 474), (264, 460), (264, 414),
             (310, 385), (62, 326), (346, 386), (369, 436), (395, 388), (391, 448), (397, 457), (375, 503), (388, 515),
             (365, 502), (403, 559), (436, 496), (421, 511), (490, 478), (467, 433), (470, 366), (434, 383), (464, 332),
             (447, 279), (424, 332), (393, 312), (391, 342), (492, 281), (496, 292),(490, 239), (396, 227), (526, 255),
             (377, 364), (558, 300), (537, 306), (513, 316), (338, 167), (240, 175), (385, 198), (566, 256), (444, 296)]
    draw_all_towns(window, town_color, towns)
    pygame.display.flip()

    used_towns = []
    town_and_cords = get_random_towns('Asia')
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
                    used_towns.append(town_and_cords[0])
                    pygame.draw.circle(window, 'green', (int(cords[0]), int(cords[1])), 4)
                town_and_cords = get_random_towns('Asia')
                cords = town_and_cords[1].split(', ')
                while True:
                    if town_and_cords[0] in used_towns:
                        town_and_cords = get_random_towns('Asia')
                        cords = town_and_cords[1].split(', ')
                    else:
                        break

            pygame.draw.rect(window, 'grey', (560, 440, 230, 150))
            text_town = font.render(town_and_cords[0], True, 'black')
            window.blit(text_town, (560, 450))
            text_kol = font.render(('Счёт:' + str(kol)), True, 'black')
            window.blit(text_kol, (560, 500))
        pygame.display.flip()


def Game_Europe():
    kol = 0
    tip = 'Europe'
    pygame.display.set_caption('Игра')
    window.blit(Europe_image, (0, 0))

    pygame.draw.rect(window, 'grey', (560, 440, 230, 150))

    town_color = 'brown'
    towns = [(350, 464), (359, 529), (355, 407), (542, 475), (243, 296), (220, 453), (113, 491), (484, 527), (407, 371),
             (381, 341), (366, 248), (354, 188), (474, 233), (479, 196), (484, 266), (522, 183), (430, 387), (83, 456),
             (306, 379), (286, 385), (288, 293), (151, 456), (258, 346), (281, 318), (365, 300), (437, 309), (137, 48),
             (397, 373), (379, 404), (188, 252), (632, 246), (588, 98), (513, 282), (546, 325), (412, 200), (482, 179),
             (589, 416), (529, 382), (508, 426), (477, 457), (447, 430), (455, 473), (435, 483), (438, 267), (428, 460),
             (392, 406), (419, 439), (654, 409), (208, 392), (206, 281), (229, 218), (113, 391), (340, 283), (316, 332),
             (347, 367), (403, 351), (426, 276), (539, 212), (644, 360), (101, 424), (473, 309), (485, 357), (556, 387),
             (301, 410), (323, 406), (375, 485), (295, 335), (288, 430), (349, 433), (523, 454), (523, 51), (556, 156)]
    draw_all_towns(window, town_color, towns)
    pygame.display.flip()

    used_towns = []
    town_and_cords = get_random_towns('Europe')
    cords = town_and_cords[1].split(', ')
    text_town = font.render(town_and_cords[0], True, 'black')
    window.blit(text_town, (560, 450))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if abs(mouse_x - int(cords[0])) < 5 and abs(mouse_y - int(cords[1])) < 5:
                    kol += 1
                    used_towns.append(town_and_cords[0])
                    pygame.draw.circle(window,'green', (int(cords[0]), int(cords[1])), 4)
                town_and_cords = get_random_towns('Europe')
                cords = town_and_cords[1].split(', ')
                while True:
                    if town_and_cords[0] in used_towns:
                        town_and_cords = get_random_towns('Europe')
                        cords = town_and_cords[1].split(', ')
                    else:
                        break
            pygame.draw.rect(window, 'grey', (560, 440, 230, 150))
            text_town = font.render(town_and_cords[0], True, 'black')
            window.blit(text_town, (560, 450))
            text_kol = font.render(('Счёт:' + str(kol)), True, 'black')
            window.blit(text_kol, (560, 500))
        pygame.display.flip()


def end(res_game):
    pygame.display.set_caption('Конец игры')
    window.fill('white', (0, 0, window_width, window_height))
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
