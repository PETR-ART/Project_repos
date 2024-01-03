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


pygame.init()

# Размер окна
window_width, window_height = 800, 600

# Создание окна
window = pygame.display.set_mode((window_width, window_height))

# Загрузка изображения
start_image = pygame.transform.scale(load_image('start_image.jpg'), (window_width, window_height))
first_image = pygame.transform.scale(load_image('first_image.webp'), (window_width, window_height))
America_image = pygame.transform.scale(load_image('America.jpg'), (window_width, window_height))
Europe_image = pygame.transform.scale(load_image('Europe.jpg'), (window_width, window_height))
Asia_image = pygame.transform.scale(load_image('Asia.jpg'), (window_width, window_height))

# Позиция и размеры кнопок
button_width, button_height = 100, 40
button_x = window_width // 2 - button_width // 2
button_start_y = window_height // 2 - button_height // 2 - 80
button_rating_y = window_height // 2 - button_height // 2
button_exit_y = window_height // 2 - button_height // 2 + 80

# Размеры кнопок окна старт
log_width = window_width // 2
log_height = window_height - (window_height - 100)
input_width = window_width * 0.2
input1_width = (window_width - input_width) // 2
input_height = window_height * 0.4

# Флаги для отслеживания состояния игры и нажатых кнопок
running = True
menu = True
start = False
cont = True
rating = False
check_settings = False
Go_Europe = False
Go_America = False
Go_Asia = False

# Флаги Настроек Стран
Europe = False
America = False
Asia = False
# Флаги Цвета Кнопок У Стран
Europe_color = 'brown'
America_color = 'brown'
Asia_color = 'brown'
# Флаги Настроек Режима
Flags = False
Countries = False
Facts = False
# Флаги Цвета Кнопок У Настроек Режима
Flags_color = 'brown'
Countries_color = 'brown'
Facts_color = 'brown'

# запуск
while running:
    for event in pygame.event.get():
        # выход из игры
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print((mouse_x, mouse_y))
            # Проверка нажатия кнопок в меню
            if menu:
                if button_x <= mouse_x <= button_x + button_width:
                    if button_start_y <= mouse_y <= button_start_y + button_height:
                        menu = False
                        start = True
                    elif button_rating_y <= mouse_y <= button_rating_y + button_height:
                        menu = False
                        rating = True
                    elif button_exit_y <= mouse_y <= button_exit_y + button_height:
                        running = False
            # Проверка нажатия кнопок в стартовом окне
            if start:
                if 310 <= mouse_x <= 490 and 355 <= mouse_y <= 400:
                    start = False
                    check_settings = True
                if 310 <= mouse_x <= 490 and 425 <= mouse_y <= 470:
                    start = False
                    menu = True
            # Проверка нажатия кнопок в окне выбора режима
            if check_settings:
                if 310 <= mouse_x <= 490 and 485 <= mouse_y <= 530:
                    check_settings = False
                    start = True

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

                if 100 <= mouse_x <= 280 and 240 <= mouse_y <= 280:
                    if Flags:
                        Flags_color = 'brown'
                        Flags = False
                    else:
                        Flags_color = 'red'
                        Flags = True

                if 300 <= mouse_x <= 480 and 240 <= mouse_y <= 280:
                    if Countries:
                        Countries_color = 'brown'
                        Countries = False
                    else:
                        Countries_color = 'red'
                        Countries = True

                if 500 <= mouse_x <= 680 and 240 <= mouse_y <= 280:
                    if Facts:
                        Facts_color = 'brown'
                        Facts = False
                    else:
                        Facts_color = 'red'
                        Facts = True

                if 310 <= mouse_x <= 490 and 415 <= mouse_y <= 460:
                    if America_color == 'red' and Asia_color == 'brown' and Europe_color == 'brown':
                        Go_America = True
                        check_settings = False
                    if Asia_color == 'red' and America_color == 'brown' and Europe_color == 'brown':
                        Go_Asia = True
                        check_settings = False
                    if Europe_color == 'red' and America_color == 'brown' and Asia_color == 'brown':
                        Go_Europe = True
                        check_settings = False
                    else:
                        print('WARNING')


            # Проверка нажатия кнопок в окне рейтинга
            if rating:
                if 310 <= mouse_x <= 490 and 485 <= mouse_y <= 530:
                    rating = False
                    menu = True

    if Go_America:
        pygame.display.set_caption('Америка')
        window.blit(America_image, (0, 0))

    if Go_Europe:
        pygame.display.set_caption('Европа')
        window.blit(Europe_image, (0, 0))

    if Go_Asia:
        pygame.display.set_caption('Азия')
        window.blit(Asia_image, (0, 0))

    # Отображение главного меню
    if menu:
        pygame.display.set_caption("Старт")

        window.blit(start_image, (0, 0))

        # Отображение кнопок
        pygame.draw.rect(window, 'brown', (button_x, button_start_y, button_width, button_height))
        pygame.draw.rect(window, 'brown', (button_x, button_rating_y, button_width, button_height))
        pygame.draw.rect(window, 'brown', (button_x, button_exit_y, button_width, button_height))

        # Отображение текста
        font = pygame.font.Font(None, 38)
        text_start = font.render("Старт", True, 'white')
        text_rating = font.render("Рейтинг", True, 'white')
        text_exit = font.render("Выход", True, 'white')

        # Размещение текста
        window.blit(text_start, (button_x + button_width // 2 - text_start.get_width() // 2,
                                 button_start_y + button_height // 2 - text_start.get_height() // 2))
        window.blit(text_rating, (button_x + button_width // 2 - text_rating.get_width() // 2,
                                  button_rating_y + button_height // 2 - text_rating.get_height() // 2))
        window.blit(text_exit, (button_x + button_width // 2 - text_exit.get_width() // 2,
                                button_exit_y + button_height // 2 - text_exit.get_height() // 2))

    # Отображение игры после нажатия на кнопку Старт
    if start:
        # Отображение заголовка
        pygame.display.set_caption("Инициализация")

        window.blit(first_image, (0, 0))

        # Отображение текста "Введите логин"
        text_log = font.render('Введите логин', True, 'Brown')
        window.blit(text_log, (log_width - 90, log_height - 10, log_width, log_height))

        # Отображение окна для ввода логина
        pygame.draw.rect(window, 'brown', (input_width, input_height,  window_width - input1_width, 100))

        # Отображение кнопок
        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y - 5, button_width + 80, button_height + 5))
        text_continue = font.render("Продолжить", True, 'white')
        window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                    button_exit_y + button_height // 2 - text_continue.get_height() // 2))

        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 65, button_width + 80, button_height + 5))
        text_back = font.render("Назад", True, 'white')
        window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                                button_exit_y + button_height // 2 - text_back.get_height() // 2 + 70))

    # Отображение игры после нажатия на кнопку Рейтинг
    if rating:
        # Отображение заголовка
        pygame.display.set_caption("Рейтинг")

        window.blit(first_image, (0, 0))

        # Отображение текста "Выберите режим"
        text_check = font.render('Рекорды', True, 'Brown')
        window.blit(text_check, (350, 60, 400, 80))

        # Отображение кнопок
        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 125, button_width + 80, button_height + 5))
        text_back = font.render("Назад", True, 'white')
        window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                                button_exit_y + button_height // 2 - text_back.get_height() // 2 + 130))

    if check_settings:
        # Отображение заголовка
        pygame.display.set_caption("Выбор Режима")

        window.blit(first_image, (0, 0))

        # Отображение текста "Выберите режим"
        text_check = font.render('Выберите режим', True, 'Brown')
        window.blit(text_check, (310, 60, 400, 80))

        # Отображение кнопок
        pygame.draw.rect(window, Europe_color, (button_x - 250, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Европа", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 210,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, America_color, (button_x - 50, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Америка", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 10,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, Asia_color, (button_x + 150, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Азия", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 + 190,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, Flags_color,
                         (button_x - 250, button_exit_y - 120, button_width + 80, button_height + 5))
        text_europe = font.render("Флаги", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 210,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 118))

        pygame.draw.rect(window, Countries_color,
                         (button_x - 50, button_exit_y - 120, button_width + 80, button_height + 5))
        text_europe = font.render("Страны", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 10,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 118))

        pygame.draw.rect(window, Facts_color,
                         (button_x + 150, button_exit_y - 120, button_width + 80, button_height + 5))
        text_europe = font.render("Факты", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 + 190,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 118))

        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 55, button_width + 80, button_height + 5))
        text_continue = font.render("Продолжить", True, 'white')
        window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                    button_exit_y + button_height // 2 - text_continue.get_height() // 2 + 60))

        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 125, button_width + 80, button_height + 5))
        text_back = font.render("Назад", True, 'white')
        window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                                button_exit_y + button_height // 2 - text_back.get_height() // 2 + 130))

    # Обновление окна
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()
