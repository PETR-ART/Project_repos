import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data/images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        pygame.quit()

    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()

# Размер окна
window_width = 800
window_height = 600

# Создание окна
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Окно Старта")

# Загрузка изображения
start_image = load_image('start_image.jpg')

# Позиция и размеры кнопок
button_width = 100
button_height = 40
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_width:
                    if button_start_y <= mouse_y <= button_start_y + button_height:
                        menu = False
                        start = True
                    elif button_rating_y <= mouse_y <= button_rating_y + button_height:
                        menu = False
                        rating = True
                    elif button_exit_y <= mouse_y <= button_exit_y + button_height:
                        running = False

    # Отображение главного меню
    if menu:
        # Очистка экрана
        window.fill('black')

        # Отображение изображения
        #window.blit(start_image, (0, 0))
        fon = pygame.transform.scale(load_image('start_image.jpg'), (window_width, window_height))
        window.blit(fon, (0, 0))

        # Отображение кнопок
        pygame.draw.rect(window, 'brown', (button_x, button_start_y, button_width, button_height))
        pygame.draw.rect(window, 'brown', (button_x, button_rating_y, button_width, button_height))
        pygame.draw.rect(window, 'brown', (button_x, button_exit_y, button_width, button_height))

        # Отображение текста
        font = pygame.font.Font(None, 36)
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

    # Отображение игры после нажатия на кнопку "Start"
    if start:
        # Очистка экрана и закраска его жёлтым цветом + заголовок окна
        window.fill('yellow')
        pygame.display.set_caption("Окно инициализации")

        # Отображение текста "Введите логин"
        text_log = font.render('Введите логин', True, 'white')
        window.blit(text_log, (log_width - 90, log_height - 10, log_width, log_height))

        # Отображение окна для ввода логина
        pygame.draw.rect(window, 'brown', (input_width, input_height,  window_width - input1_width, 100))

        #Отображение кнопки продолжения
        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y - 5, button_width + 80, button_height + 5))
        text_continue = font.render("Продолжить", True, 'white')
        window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                    button_exit_y + button_height // 2 - text_continue.get_height() // 2))


    # Отображение игры после нажатия на кнопку Рейтинг
    if rating:
        # Очистка экрана и закраска его красным цветом
        window.fill('red')
        pygame.display.set_caption("Окно рекордов")

    # Обновление окна
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()
