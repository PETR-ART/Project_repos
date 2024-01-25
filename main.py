import sqlite3

import random
import pygame
import os


# Логин игрока
LOGIN = ''

# количество раундов
N = 10

# Подключение к базе данных
conn = sqlite3.connect('comandproject.db')
cursor = conn.cursor()

# словари со странами
America = {'США': 'USA', 'Канада': 'Canada', 'Мексика': 'Mexico', 'Куба': 'Cuba'}
Asia = {'Япония': 'Japan', 'Китай': 'China', 'Индия': 'India', 'Индонезия': 'Indonesia'}
Europe = {'Россия': 'Russia', 'Германия': 'Germany', 'Италия': 'Itali', 'Казахстан': 'Kazahstan'}


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


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, color='brown', text_color='white', font_size=38):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.color = color
        self.image.fill(pygame.Color(self.color))
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.text_color = text_color

    def update_text(self, text):
        self.text = text

    def update_color(self, color):
        self.color = color

    def update_text_color(self, text_color):
        self.text_color = text_color

    def draw(self, window):
        text = self.font.render(self.text, True, self.text_color)
        text_width, text_height = text.get_size()
        x_offset = (self.rect.width - text_width) // 2
        y_offset = (self.rect.height - text_height) // 2
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(text, (self.rect.x + x_offset, self.rect.y + y_offset))


# написание текста
def print_text(message, x, y, color='white', font_size=38):
    font = pygame.font.Font(None, font_size)
    text = font.render(message, True, color)
    window.blit(text, (x, y))


# для загрузки файлов
def load_image(name, colorkey=None):
    # Полный путь к файлу
    fullname = os.path.join('data/images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        pygame.quit()
        quit()

    # загружаем картинку
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


# Получить случайную страну
def get_random_country_eng(type):
    if type:
        if type == 'Europe':
            random_country_rus = random.choice(list(Europe.keys()))
        elif type == 'Asia':
            random_country_rus = random.choice(list(Asia.keys()))
        elif type == 'America':
            random_country_rus = random.choice(list(America.keys()))
        random_country_eng = ""
        # и её английское название
        if random_country_rus in Europe:
            random_country_eng = Europe[random_country_rus]
        elif random_country_rus in Asia:
            random_country_eng = Asia[random_country_rus]
        else:
            random_country_eng = America[random_country_rus]
        # и ещё 3 страны для вариантов ответа
        new_random_countries_rus = random.sample(list(Europe.keys()) + list(Asia.keys()) + list(America.keys()), k=3)
        while random_country_rus in new_random_countries_rus:
            new_random_countries_rus = random.sample(list(Europe.keys()) + list(Asia.keys()) + list(America.keys()),
                                                     k=3)
        # добавляем нашу страну к списку
        random_countries_rus = new_random_countries_rus + [random_country_rus]
        # и перемешиваем список
        random.shuffle(random_countries_rus)
        return random_country_eng, random_country_rus, random_countries_rus


# получить случайный город в зависимости от типа
def get_random_towns(type):
    if type == 'Европа':
        random_town = random.choice(list(towns_europe))
        random_town_cords = towns_europe[random_town]
    if type == 'Америка':
        random_town = random.choice(list(towns_America))
        random_town_cords = towns_America[random_town]
    if type == 'Азия':
        random_town = random.choice(list(towns_Asia))
        random_town_cords = towns_Asia[random_town]

    return random_town, random_town_cords


# инициализация игры
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

start_image = pygame.transform.scale(load_image('start_image.png'), window_size)
first_image = pygame.transform.scale(load_image('first_image.png'), window_size)
America_image = pygame.transform.scale(load_image('town/America.jpg'), window_size)
Europe_image = pygame.transform.scale(load_image('town/Europe.jpg'), window_size)
Asia_image = pygame.transform.scale(load_image('town/Asia.jpg'), window_size)


# начальное меню
def Menu():
    pygame.display.set_caption("Меню")
    window.blit(start_image, (0, 0))

    button_start_sprite = Sprite(button_x, button_start_y, button_width, button_height, "Старт")
    button_rating_sprite = Sprite(button_x - 5, button_rating_y, button_width + 10, button_height, "Рейтинг", font_size=36)
    button_exit_sprite = Sprite(button_x, button_exit_y, button_width, button_height, "Выход")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_start_sprite.rect.collidepoint(mouse_pos):
                    Start()
                elif button_rating_sprite.rect.collidepoint(mouse_pos):
                    Rating()
                elif button_exit_sprite.rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

        button_start_sprite.draw(window)
        button_rating_sprite.draw(window)
        button_exit_sprite.draw(window)

        pygame.display.flip()


# окно начала с выбором режима входа
def Start():
    pygame.display.set_caption("Инициализация")
    window.blit(first_image, (0, 0))

    button_enter_sprite = Sprite(button_x - 120, button_start_y, button_width + 30, button_height + 10, "Вход")
    button_register_sprite = Sprite(button_x + 70, button_start_y, button_width + 100, button_height + 10,
                                    "Регистрация")
    button_back_sprite = Sprite(button_x - 40, button_exit_y + 65, button_width + 80, button_height + 5, "Назад")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if button_enter_sprite.rect.collidepoint(mouse_pos):
                    Enter()

                if button_register_sprite.rect.collidepoint(mouse_pos):
                    Register()

                if button_back_sprite.rect.collidepoint(mouse_pos):
                    Menu()

        button_enter_sprite.draw(window)
        button_register_sprite.draw(window)
        button_back_sprite.draw(window)

        pygame.display.flip()


# регистрация
def Register():
    global LOGIN
    pygame.display.set_caption("Регистрация")
    window.blit(first_image, (0, 0))

    button_login_sprite = Sprite(button_x - 100, button_start_y - 50, button_width + 200, button_height + 15,
                                 "Введите логин", text_color="dark grey", font_size=40)
    button_password_sprite = Sprite(button_x - 100, button_start_y + 20, button_width + 200, button_height + 15,
                                    "Введите пароль", text_color="dark grey", font_size=40)
    button_next_sprite = Sprite(button_x - 40, button_exit_y - 5, button_width + 80, button_height + 5, "Продолжить")
    button_back_sprite = Sprite(button_x - 40, button_exit_y + 65, button_width + 80, button_height + 5, "Назад")

    button_enter_sprite = Sprite(button_x - 250, button_start_y - 165, button_width + 500, button_height + 10,
                                 "Введите Логин и Пароль", color='white', text_color="red")

    login = '|'
    password = '|'

    need_input_login = False
    need_input_password = False

    tick = 1000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                tick = 1000
                login = login.replace('|', '')
                password = password.replace('|', '')

                if event.key == pygame.K_RETURN:
                    if need_input_login:
                        need_input_login = False
                    if need_input_password:
                        need_input_password = False

                elif event.key == pygame.K_BACKSPACE:
                    if need_input_login:
                        login = login[:-1]
                    if need_input_password:
                        password = password[:-1]
                else:
                    if need_input_login:
                        if len(login) <= 15:
                            login += event.unicode
                    if need_input_password:
                        if len(password) <= 15:
                            password += event.unicode

                login += '|'
                password += '|'

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if button_login_sprite.rect.collidepoint(mouse_pos):
                    need_input_login = True
                    need_input_password = False

                if button_password_sprite.rect.collidepoint(mouse_pos):
                    need_input_password = True
                    need_input_login = False

                if button_next_sprite.rect.collidepoint(mouse_pos):
                    text = ''

                    need_input_login = False
                    need_input_password = False

                    login = login.replace('|', '')
                    password = password.replace('|', '')

                    if login != '' and password != '':
                        try:
                            # Проверка наличия логина в базе данных
                            cursor.execute("SELECT login FROM setting WHERE login=?", (login,))
                            result = cursor.fetchone()
                            # Если логина нет, добавляем его в базу данных
                            if result is None:
                                if password is not None:
                                    cursor.execute("INSERT INTO setting (login, password, mod_eng," 
                                                   " mod_flag, mod_town) VALUES (?, ?, '', '', '')", (login, password))
                                    conn.commit()
                                    text = "Успешно!"
                                    LOGIN = login
                                    Check_setting()
                                else:
                                    text = "Ошибка! Введите что-то в строку пароль!"
                            else:
                                text = "Ошибка! Такой логин уже существует"

                            # Закрытие соединения с базой данных
                            conn.close()

                        except sqlite3.Error:
                            text = "Ошибка! Попробуйте снова!"

                    else:
                        text = "Ошибка! Введите логин и пароль"

                    button_enter_sprite.update_text(text)

                if button_back_sprite.rect.collidepoint(mouse_pos):
                    Start()

        tick -= 1
        if tick == 0:
            login = login[:-1]
            password = password[:-1]
        if tick == -1000:
            login += '|'
            password += '|'
            tick = 1000

        if need_input_login:
            button_login_sprite.update_text(login)
            button_login_sprite.update_text_color('white')

        elif login == '' and not need_input_login:
            button_login_sprite.update_text("Введите логин")
            button_login_sprite.update_text_color("dark grey")

        if need_input_password:
            button_password_sprite.update_text(password)
            button_password_sprite.update_text_color('white')

        elif password == '' and not need_input_password:
            button_password_sprite.update_text("Введите пароль")
            button_password_sprite.update_text_color("dark grey")

        button_login_sprite.draw(window)
        button_password_sprite.draw(window)
        button_next_sprite.draw(window)
        button_back_sprite.draw(window)
        button_enter_sprite.draw(window)

        pygame.display.flip()


# вход
def Enter():
    global LOGIN
    pygame.display.set_caption("Вход")
    window.blit(first_image, (0, 0))

    button_login_sprite = Sprite(button_x - 100, button_start_y - 50, button_width + 200, button_height + 15,
                                 "Введите логин", text_color="dark grey", font_size=40)
    button_password_sprite = Sprite(button_x - 100, button_start_y + 20, button_width + 200, button_height + 15,
                                    "Введите пароль", text_color="dark grey", font_size=40)
    button_next_sprite = Sprite(button_x - 40, button_exit_y - 5, button_width + 80, button_height + 5, "Продолжить")
    button_back_sprite = Sprite(button_x - 40, button_exit_y + 65, button_width + 80, button_height + 5, "Назад")

    button_enter_sprite = Sprite(button_x - 250, button_start_y - 165, button_width + 500, button_height + 10,
                                 "Введите Логин и Пароль", color='white', text_color="red")

    login = '|'
    password = '|'

    need_input_login = False
    need_input_password = False

    tick = 1000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                tick = 1000
                login = login.replace('|', '')
                password = password.replace('|', '')

                if event.key == pygame.K_RETURN:
                    if need_input_login:
                        need_input_login = False
                    if need_input_password:
                        need_input_password = False

                elif event.key == pygame.K_BACKSPACE:
                    if need_input_login:
                        login = login[:-1]
                    if need_input_password:
                        password = password[:-1]
                else:
                    if need_input_login:
                        if len(login) <= 15:
                            login += event.unicode
                    if need_input_password:
                        if len(password) <= 15:
                            password += event.unicode

                login += '|'
                password += '|'

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if button_login_sprite.rect.collidepoint(mouse_pos):
                    need_input_login = True
                    need_input_password = False

                if button_password_sprite.rect.collidepoint(mouse_pos):
                    need_input_password = True
                    need_input_login = False

                if button_next_sprite.rect.collidepoint(mouse_pos):
                    text = ''

                    need_input_login = False
                    need_input_password = False

                    login = login.replace('|', '')
                    password = password.replace('|', '')

                    if login != '' and password != '':
                        try:
                            # Проверка наличия логина в базе данных
                            cursor.execute("SELECT password FROM setting WHERE login=?", (login,))
                            result = cursor.fetchone()
                            # Если логина нет, добавляем его в базу данных
                            if result is not None:
                                if result[0] == password:
                                    text = "Успешно!"
                                    LOGIN = login
                                    Check_setting()
                                else:
                                    text = "Ошибка! Неправильный пароль!"
                            else:
                                text = "Ошибка! Логин не найден"

                            # Закрытие соединения с базой данных
                            conn.close()

                        except sqlite3.Error:
                            text = "Ошибка! Попробуйте снова!"

                    else:
                        text = "Ошибка! Введите логин и пароль"

                    # Закрытие соединения с базой данных
                    conn.close()

                    button_enter_sprite.update_text(text)

                if button_back_sprite.rect.collidepoint(mouse_pos):
                    Start()

        tick -= 1
        if tick == 0:
            login = login[:-1]
            password = password[:-1]
        if tick == -1000:
            login += '|'
            password += '|'
            tick = 1000

        if need_input_login:
            button_login_sprite.update_text(login)
            button_login_sprite.update_text_color('white')

        elif login == '' and not need_input_login:
            button_login_sprite.update_text("Введите логин")
            button_login_sprite.update_text_color("dark grey")

        if need_input_password:
            button_password_sprite.update_text(password)
            button_password_sprite.update_text_color('white')

        elif password == '' and not need_input_password:
            button_password_sprite.update_text("Введите пароль")
            button_password_sprite.update_text_color("dark grey")

        button_login_sprite.draw(window)
        button_password_sprite.draw(window)
        button_next_sprite.draw(window)
        button_back_sprite.draw(window)
        button_enter_sprite.draw(window)

        pygame.display.flip()


# функция написания рейтинга для нужного мода
def print_rating(name, mode, x, y):
    cursor.execute(f"SELECT login, {mode} FROM setting ORDER BY {mode} DESC LIMIT 5")
    rows = cursor.fetchall()

    header = f"{name.capitalize()}"
    print_text(header, x, y, color='brown')

    row_y = 50
    for row in rows:
        login, percentage = row
        if not percentage:
            percentage = 0
        print_text(f'{login[:6]} - {percentage}%', x, y + row_y, color='red')
        row_y += 50


# рейтинг
def Rating():
    pygame.display.set_caption("Рейтинг")
    window.blit(first_image, (0, 0))

    button_enter = pygame.Rect(button_x - 250, button_start_y - 165, button_width + 500, button_height + 350)
    pygame.draw.rect(window, 'white', button_enter)

    print_text("Рекорды", window_width // 2 - 65, button_start_y - 150, color='red')

    button_back_sprite = Sprite(button_x - 40, button_exit_y + 125, button_width + 80, button_height + 5, "Назад")

    print_rating('Eng', 'mod_eng', 110, 100)
    print_rating('Flag', 'mod_flag', 310, 100)
    print_rating('Town', 'mod_town', 510, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_back_sprite.rect.collidepoint(mouse_pos):
                    Menu()

        button_back_sprite.draw(window)

        pygame.display.flip()


# выбор режима игры
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

    button_enter_sprite = Sprite(button_x - 250, button_start_y - 165, button_width + 500, button_height + 10,
                                 "Выберите режим", color="white", text_color='brown')

    while True:
        # Отображение кнопок
        button_Europe_sprite = Sprite(button_x - 250, button_exit_y - 220, button_width + 80, button_height + 5,
                                        "Европа", color=Europe_color)
        button_America_sprite = Sprite(button_x - 50, button_exit_y - 220, button_width + 80, button_height + 5,
                                      "Америка", color=America_color)
        button_Asia_sprite = Sprite(button_x + 150, button_exit_y - 220, button_width + 80, button_height + 5,
                                      "Азия", color=Asia_color)

        button_Flags_sprite = Sprite(button_x - 200, button_exit_y - 120, button_width + 80, button_height + 5,
                                    "Флаги", color=Flags_color)
        button_Town_sprite = Sprite(button_x + 80, button_exit_y - 120, button_width + 80, button_height + 5,
                                    "Города", color=Town_color)
        button_Eng_sprite = Sprite(button_x - 120, button_exit_y - 40, button_width + 200, button_height + 5,
                                    "Английские Названия", color=Eng_color)

        button_next_sprite = Sprite(button_x - 40, button_exit_y + 55, button_width + 80, button_height + 5, "Продолжить")
        button_back_sprite = Sprite(button_x - 40, button_exit_y + 125, button_width + 80, button_height + 5, "Назад")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if button_back_sprite.rect.collidepoint(mouse_pos):
                    Start()

                if button_Europe_sprite.rect.collidepoint(mouse_pos):
                    if Europe:
                        Europe_color = 'brown'
                        Europe = False
                    else:
                        Europe_color = 'red'
                        America_color = 'brown'
                        Asia_color = 'brown'
                        Europe = True

                if button_America_sprite.rect.collidepoint(mouse_pos):
                    if America:
                        America_color = 'brown'
                        America = False
                    else:
                        America_color = 'red'
                        Europe_color = 'brown'
                        Asia_color = 'brown'
                        America = True

                if button_Asia_sprite.rect.collidepoint(mouse_pos):
                    if Asia:
                        Asia_color = 'brown'
                        Asia = False
                    else:
                        Asia_color = 'red'
                        America_color = 'brown'
                        Europe_color = 'brown'
                        Asia = True

                if button_Flags_sprite.rect.collidepoint(mouse_pos):
                    if mod_flag:
                        Flags_color = 'brown'
                        mod_flag = False
                    else:
                        Flags_color = 'red'
                        Eng_color = 'brown'
                        Town_color = 'brown'
                        mod_flag = True

                if button_Town_sprite.rect.collidepoint(mouse_pos):
                    if mod_towns:
                        Town_color = 'brown'
                        mod_towns = False
                    else:
                        Town_color = 'red'
                        Flags_color = 'brown'
                        Eng_color = 'brown'
                        mod_towns = True

                if button_Eng_sprite.rect.collidepoint(mouse_pos):
                    if mod_eng:
                        Eng_color = 'brown'
                        mod_eng = False
                    else:
                        Eng_color = 'red'
                        Flags_color = 'brown'
                        Town_color = 'brown'
                        mod_eng = True

                if button_next_sprite.rect.collidepoint(mouse_pos):
                    if Europe and Europe_color == 'red' and mod_towns and Town_color == 'red':
                        Game_Europe()
                    if America and America_color == 'red' and mod_towns and Town_color == 'red':
                        Game_America()
                    if Asia and Asia_color == 'red' and mod_towns and Town_color == 'red':
                        Game_Asia()

                    type1 = ''
                    type2 = ''

                    if Europe and Europe_color == 'red':
                        type1 = 'Europe'
                    if America and America_color == 'red':
                        type1 = 'America'
                    if Asia and Asia_color == 'red':
                        type1 = 'Asia'

                    if mod_eng and Eng_color == 'red':
                        type2 = 'mod_eng'
                    elif mod_flag and Flags_color == 'red':
                        type2 = 'mod_flag'

                    if type1 and type2:
                        Game(type1, type2)

        button_Europe_sprite.draw(window)
        button_America_sprite.draw(window)
        button_Asia_sprite.draw(window)
        button_Flags_sprite.draw(window)
        button_Town_sprite.draw(window)
        button_Eng_sprite.draw(window)
        button_next_sprite.draw(window)
        button_back_sprite.draw(window)
        button_enter_sprite.draw(window)

        pygame.display.flip()


# начало игры, режимы: английские названия и флаги
def Game(type1, type2):
    global LOGIN
    pygame.display.set_caption('Игра')

    # количество раундов
    round = N

    clock = pygame.time.Clock()
    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1500)

    # Переменная для хранения неправильной кнопки
    wrong_button = False
    is_wrong_answer = False
    wrong_answer = 0

    # Главный цикл программы
    new_round = True
    while round != -1:
        window.fill('white')

        if new_round:
            round -= 1
            counter, text = 10, str(counter).rjust(3)
            random_country_eng, random_country_rus, random_countries_rus = get_random_country_eng(type1)

            sprite_sprites = pygame.sprite.Group()
            sprite_positions = [(100, 200), (100, 300), (500, 200), (500, 300)]
            for i in range(4):
                sprite = Sprite(sprite_positions[i][0], sprite_positions[i][1], 200, 50, random_countries_rus[i])
                sprite_sprites.add(sprite)

            wrong_button = False
            is_wrong_answer = False
            new_round = False

        if round == -1:

            percent = int((N - wrong_answer) / N) * 100

            # Обновление значения процента в выбранном режиме
            cursor.execute(f"UPDATE setting SET {type2} = ? WHERE login = ?", (percent, LOGIN))
            conn.commit()

            # Закрытие соединения с базой данных
            conn.close()

            end(res_game='Победа!')

        if 'mod_flag' in type2 and 'mod_eng' not in type2:
            flag = pygame.transform.scale(pygame.image.load('data/images/' + type1 + '/Flag_' + random_country_eng + '.png'),
                                          (window_width, window_height))
            flag_rect = flag.get_rect()
            window.blit(flag, flag_rect)

        elif 'mod_flag' not in type2 and 'mod_eng' in type2:
            print_text(random_country_eng, window_width / 2 - 60, 50, color='black', font_size=60)

        for sprite in sprite_sprites:
            sprite.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    end(res_game='Ты проиграл!')
                is_wrong_answer = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for sprite in sprite_sprites:
                    if sprite.rect.collidepoint(mouse_pos):
                        if sprite.text == random_country_rus:
                            new_round = True
                        else:
                            wrong_button = True
                            is_wrong_answer = True

            if is_wrong_answer:
                if wrong_button:
                    if counter > 5:
                        counter -= 5
                    else:
                        counter = 0
                    text = str(counter).rjust(3)
                    wrong_answer += 1
                    is_wrong_answer = False

        pygame.draw.rect(window, 'grey', (720, 0, 800, 40))
        window.blit(font.render(text, True, (0, 0, 0)), (720, 10))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)


# нарисовать город
def draw_town(window, town_color, x, y):
    pygame.draw.circle(window, town_color, (x, y), 4)


# нарисовать города
def draw_all_towns(window, town_color, towns):
    for town in towns:
        draw_town(window, town_color, town[0], town[1])


# режим города Америки
def Game_America():
    type = 'Америка'
    game(type, America_image,
         [(458, 254), (472, 246), (487, 239), (437, 302), (393, 289), (432, 312), (253, 272), (241, 259), (235, 212),
          (520, 232), (489, 220), (444, 235), (356, 208), (352, 277), (372, 256), (108, 158), (239, 221), (362, 292),
          (460, 322), (487, 326), (454, 328), (432, 281), (436, 266), (419, 274), (445, 395), (464, 366), (501, 353),
          (545, 368), (557, 370), (444, 357), (391, 337), (412, 348), (423, 355), (449, 385), (459, 428), (498, 436),
          (548, 468), (548, 504), (555, 501), (489, 464), (486, 500), (509, 499), (578, 143), (472, 228), (345, 320),
          (265, 259), (273, 247), (310, 255), (343, 300), (312, 281), (301, 295), (398, 318), (592, 393), (613, 398)])


# режим города Азии
def Game_Asia():
    type = 'Азия'
    game(type, Asia_image,
         [(28, 267), (44, 279), (38, 293), (82, 269), (101, 265), (106, 277), (128, 272), (70, 312), (72, 300),
          (98, 301), (103, 320), (117, 339), (81, 369), (79, 386), (101, 425), (109, 439), (171, 378), (148, 372),
          (111, 289), (149, 346), (135, 304), (172, 298), (187, 312), (172, 287), (214, 275), (223, 269), (219, 284),
          (117, 366), (257, 253), (247, 258), (232, 206), (240, 215), (219, 304), (204, 322), (236, 315), (210, 363),
          (241, 326), (262, 342), (241, 406), (297, 353), (321, 376), (319, 355), (272, 474), (264, 460), (264, 414),
          (310, 385), (62, 326), (346, 386), (369, 436), (395, 388), (391, 448), (397, 457), (375, 503), (388, 515),
          (365, 502), (403, 559), (436, 496), (421, 511), (490, 478), (467, 433), (470, 366), (434, 383), (464, 332),
          (447, 279), (424, 332), (393, 312), (391, 342), (492, 281), (496, 292), (490, 239), (396, 227), (526, 255),
          (377, 364), (558, 300), (537, 306), (513, 316), (338, 167), (240, 175), (385, 198), (566, 256), (444, 296)])


# режим города Европы
def Game_Europe():
    type = 'Европа'
    game(type, Europe_image,
         [(350, 464), (359, 529), (355, 407), (542, 475), (243, 296), (220, 453), (113, 491), (484, 527), (407, 371),
          (381, 341), (366, 248), (354, 188), (474, 233), (479, 196), (484, 266), (522, 183), (430, 387), (83, 456),
          (306, 379), (286, 385), (288, 293), (151, 456), (258, 346), (281, 318), (365, 300), (437, 309), (137, 48),
          (397, 373), (379, 404), (188, 252), (632, 246), (588, 98), (513, 282), (546, 325), (412, 200), (482, 179),
          (589, 416), (529, 382), (508, 426), (477, 457), (447, 430), (455, 473), (435, 483), (438, 267), (428, 460),
          (392, 406), (419, 439), (654, 409), (208, 392), (206, 281), (229, 218), (113, 391), (340, 283), (316, 332),
          (347, 367), (403, 351), (426, 276), (539, 212), (644, 360), (101, 424), (473, 309), (485, 357), (556, 387),
          (301, 410), (323, 406), (375, 485), (295, 335), (288, 430), (349, 433), (523, 454), (523, 51), (556, 156)])


# начало игры, режим города
def game(type, image, towns):
    global LOGIN

    res = ''

    answers = 5
    wrong_answer = 0
    kol = 0

    pygame.display.set_caption('Игра')
    window.blit(image, (0, 0))

    pygame.draw.rect(window, 'grey', (550, 440, 250, 150))

    town_color = 'brown'
    draw_all_towns(window, town_color, towns)

    pygame.display.flip()

    used_towns = []

    town_and_cords = get_random_towns(type)
    cords = town_and_cords[1].split(', ')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if abs(mouse_x - int(cords[0])) < 5 and abs(mouse_y - int(cords[1])) < 5:
                    kol += 1
                    used_towns.append(town_and_cords[0])
                    pygame.draw.circle(window, 'green', (int(cords[0]), int(cords[1])), 4)
                else:
                    answers -= 1
                    wrong_answer += 1
                town_and_cords = get_random_towns(type)
                cords = town_and_cords[1].split(', ')
                while True:
                    if town_and_cords[0] in used_towns:
                        town_and_cords = get_random_towns(type)
                        cords = town_and_cords[1].split(', ')
                    else:
                        break

            pygame.draw.rect(window, 'grey', (550, 440, 230, 150))
            print_text(town_and_cords[0], 550, 450, color='black')

            print_text(f'Счёт: {str(kol)}', 550, 500, color='black')

            print_text(f'Число попыток: {str(answers)}', 550, 550, color='black')

            if kol == 10:
                percent = int((N - wrong_answer) / N) * 100

                # Обновление значения процента в выбранном режиме
                cursor.execute(f"UPDATE setting SET mod_town = ? WHERE login = ?", (percent, LOGIN))
                conn.commit()

                # Закрытие соединения с базой данных
                conn.close()

                if 0 <= percent < 30:
                    res = 'Плохой результат'
                elif 30 <= percent < 70:
                    res = 'Неплохой результат'
                elif 70 <= percent < 90:
                    res = 'Хороший результат'
                elif 90 <= percent <= 100:
                    res = 'Отличный результат!'
                end(res)

            if answers == 0:
                end(res_game='Ты проиграл!')

        pygame.display.flip()


# конец игры, финальное окно
def end(res_game):
    pygame.display.set_caption('Конец игры')
    window.fill('white', (0, 0, window_width, window_height))

    print_text(res_game, 50, 100, color='brown', font_size=50)

    print_text('Нажмите любую клавишу,', 50, 250, color='brown')
    print_text('чтобы выйти', 50, 300, color='brown')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                Menu()

        pygame.display.flip()


# запуск игры
Menu()
